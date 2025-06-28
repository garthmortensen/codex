#!/usr/bin/env python3
"""
Textual Cheatsheet Manager
Usage: python3 ~/cheatsheets/cheatsheets.py
"""

import sys
from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (
    Header, Footer, ListView, ListItem, Label, 
    Markdown, Static, Input
)
from textual.reactive import reactive
from textual.message import Message
from textual.binding import Binding

# Try to import newer splitter widgets, fallback to basic containers
try:
    from textual.widgets import VerticalSplitter, HorizontalSplitter
    SPLITTER_AVAILABLE = True
except ImportError:
    try:
        from textual.containers import VerticalSplitter, HorizontalSplitter  
        SPLITTER_AVAILABLE = True
    except ImportError:
        SPLITTER_AVAILABLE = False

class CheatsheetManager(App):
    """A Textual app for browsing cheatsheets"""
    
    # Set default theme to Dracula - use the correct attribute name
    DEFAULT_CSS = """
    App {
        background: $surface;
    }
    
    #sidebar {
        width: 30%;
        border-right: solid $primary;
    }
    
    #content-panel {
        width: 70%;
        padding: 1;
    }
    
    #search-input {
        margin: 1 0;
    }
    
    .list-item-label {
        padding: 0 1;
    }
    
    #status {
        height: 3;
        background: $surface;
        border-top: solid $primary;
        padding: 1;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("ctrl+f", "focus_search", "Search"),
        Binding("ctrl+d", "toggle_dark", "Toggle theme"),
    ]
    
    # Reactive attributes
    current_file = reactive(None)
    search_term = reactive("")
    
    def __init__(self, cheatsheets_dir=None):
        super().__init__()
        # Set theme in constructor
        self.theme = "dracula"
        # Default to the cheatsheets subdirectory, handling different scenarios
        if cheatsheets_dir is None:
            # Try to find the cheatsheets directory intelligently
            current_dir = Path.cwd()
            
            # Check if we're already in the project root (has pyproject.toml)
            if (current_dir / "pyproject.toml").exists() and (current_dir / "cheatsheets").exists():
                cheatsheets_dir = current_dir / "cheatsheets"
            # Check if we're in a subdirectory and need to go up to find the project root
            elif (current_dir.parent / "pyproject.toml").exists() and (current_dir.parent / "cheatsheets").exists():
                cheatsheets_dir = current_dir.parent / "cheatsheets"
            # Check if we're in the cheatsheets directory itself
            elif current_dir.name == "cheatsheets" and (current_dir / "git.md").exists():
                cheatsheets_dir = current_dir
            # Fallback to current directory / cheatsheets
            else:
                cheatsheets_dir = current_dir / "cheatsheets"
        
        self.cheatsheets_dir = Path(cheatsheets_dir)
        self.cheatsheets = {}
        self.filtered_cheatsheets = {}
        self.file_contents = {}  # Cache for file contents
        self.search_results = {}  # Cache for search results with line numbers
        
    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header(show_clock=False)
        
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Input(
                    placeholder="Search cheatsheets...", 
                    id="search-input"
                )
                yield ListView(id="cheatsheet-list")
            
            with VerticalScroll(id="content-panel"):
                yield Markdown("Select a cheatsheet to view", id="content")
        
        yield Static("Ready | Use arrow keys to navigate, Enter to select", id="status")
        yield Footer()
    
    def on_mount(self) -> None:
        """Called when app starts"""
        self.title = "Cheatsheet Manager"
        self.sub_title = str(self.cheatsheets_dir)
        # Force set the theme after mounting
        self.dark = True  # Ensure dark mode is enabled
        try:
            self.theme = "dracula"
        except Exception:
            # Fallback if dracula theme not available
            self.theme = "dark"
        self._discover_cheatsheets()
        self._update_list()
        
    def _discover_cheatsheets(self):
        """Auto-discover markdown files in cheatsheets directory"""
        self.cheatsheets = {}
        
        if not self.cheatsheets_dir.exists():
            self.query_one("#status", Static).update(
                f"Error: Directory {self.cheatsheets_dir} not found"
            )
            return
            
        for md_file in self.cheatsheets_dir.glob("*.md"):
            # Skip README.md
            if md_file.name == "README.md":
                continue
            name = md_file.stem.replace("-", " ").replace("_", " ").title()
            self.cheatsheets[name] = md_file
            
        self.filtered_cheatsheets = self.cheatsheets.copy()
        
        if self.cheatsheets:
            self.query_one("#status", Static).update(
                f"Found {len(self.cheatsheets)} cheatsheets | Use Ctrl+F to search"
            )
        else:
            self.query_one("#status", Static).update(
                "No markdown files found in directory"
            )
    
    def _update_list(self):
        """Update the ListView with current cheatsheets"""
        list_view = self.query_one("#cheatsheet-list", ListView)
        list_view.clear()
        
        if not self.filtered_cheatsheets:
            list_view.append(ListItem(Label("No cheatsheets found", classes="list-item-label")))
            return
            
        for i, (name, filepath) in enumerate(sorted(self.filtered_cheatsheets.items()), 1):
            # Check if we have search results with sections for this file
            if name in self.search_results:
                sections = self.search_results[name]
                if len(sections) == 1:
                    # Show single section name
                    label_text = f"{i:2d} - {name.lower()} ({sections[0]})"
                elif len(sections) <= 3:
                    # Show multiple section names
                    sections_str = ", ".join(sections)
                    label_text = f"{i:2d} - {name.lower()} ({sections_str})"
                else:
                    # Show first few section names if many matches
                    sections_str = ", ".join(sections[:2])
                    label_text = f"{i:2d} - {name.lower()} ({sections_str}, +{len(sections)-2})"
            else:
                label_text = f"{i:2d} - {name.lower()}"
            
            label = Label(label_text, classes="list-item-label")
            list_item = ListItem(label)
            list_item._cheatsheet_name = name
            list_item._cheatsheet_filepath = filepath
            list_view.append(list_item)
    
    def _filter_cheatsheets(self, search_term: str):
        """Filter cheatsheets based on search term in file contents"""
        if not search_term:
            self.filtered_cheatsheets = self.cheatsheets.copy()
        else:
            # Search through file contents instead of filenames
            self.filtered_cheatsheets = self._search_file_contents(search_term)

        self._update_list()
        
        # Update status
        if search_term:
            count = len(self.filtered_cheatsheets)
            self.query_one("#status", Static).update(
                f"Content search: '{search_term}' - {count} files contain this text"
            )
        else:
            self.query_one("#status", Static).update(
                f"Found {len(self.cheatsheets)} cheatsheets | Use Ctrl+F to search content"
            )
    
    def _add_line_numbers_to_markdown(self, content: str) -> str:
        """Add line numbers to markdown content with proper line breaks"""
        lines = content.split('\n')
        numbered_lines = []
        
        for i, line in enumerate(lines, 1):
            # Use a format that preserves line breaks and doesn't interfere with markdown
            line_num = f"{i:4d}:"
            # Add two spaces at the end to force a line break in markdown
            numbered_lines.append(f"{line_num} {line}  ")
        
        return '\n'.join(numbered_lines)

    def _render_cheatsheet(self, filepath):
        """Render markdown file in the content panel with search term highlighting"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Get current search term from the input widget
            search_input = self.query_one("#search-input", Input)
            current_search = search_input.value.strip()
            
            # If there's a search term, highlight it in the content
            if current_search:
                content = self._highlight_search_terms(content, current_search)
            
            content_widget = self.query_one("#content", Markdown)
            content_widget.update(content)
            
            # Update status
            if current_search:
                self.query_one("#status", Static).update(
                    f"Viewing: {filepath.stem} | Search: '{current_search}' highlighted"
                )
            else:
                self.query_one("#status", Static).update(
                    f"Viewing: {filepath.stem} | Press 'r' to refresh, 'q' to quit"
                )
            
        except FileNotFoundError:
            content_widget = self.query_one("#content", Markdown)
            content_widget.update(f"## Error: File '{filepath}' not found")
        except Exception as e:
            content_widget = self.query_one("#content", Markdown)
            content_widget.update(f"## Error reading file: {e}")

    def _highlight_search_terms(self, content: str, search_term: str) -> str:
        """Highlight search terms in markdown content using markdown syntax"""
        if not search_term:
            return content
        
        import re
        
        # Use case-insensitive regex to find all occurrences
        # Use word boundaries to avoid partial matches in code blocks where possible
        pattern = re.compile(re.escape(search_term), re.IGNORECASE)
        
        # Replace matches with highlighted version using markdown bold syntax
        highlighted_content = pattern.sub(f"**{search_term}**", content)
        
        return highlighted_content

    def _load_file_contents(self):
        """Load and cache contents of all markdown files for searching"""
        self.file_contents = {}
        for name, filepath in self.cheatsheets.items():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.file_contents[name] = f.read().lower()  # Store as lowercase for case-insensitive search
            except Exception:
                self.file_contents[name] = ""  # Empty content if file can't be read

    def _find_section_for_line(self, filepath, line_number):
        """Find the markdown section/header that contains the given line number"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            current_section = "Top"  # Default section name
            
            # Work backwards from the match line to find the most recent header
            for i in range(line_number - 1, -1, -1):
                line = lines[i].strip()
                if line.startswith('#'):
                    # Extract header text, removing the # symbols and cleaning up
                    header_text = line.lstrip('#').strip()
                    # Remove .md from header if it exists (our filename headers)
                    if header_text.endswith('.md'):
                        header_text = header_text[:-3]
                    current_section = header_text
                    break
            
            return current_section
            
        except Exception:
            return "Unknown"

    def _search_file_contents(self, search_term: str):
        """Search through file contents and return matching files with sections"""
        if not search_term:
            self.search_results = {}
            return self.cheatsheets.copy()
        
        results = {}
        self.search_results = {}
        search_term_lower = search_term.lower()
        
        for name, filepath in self.cheatsheets.items():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                matching_sections = []
                for line_num, line in enumerate(lines, 1):
                    if search_term_lower in line.lower():
                        section = self._find_section_for_line(filepath, line_num)
                        if section not in matching_sections:
                            matching_sections.append(section)
                
                if matching_sections:
                    results[name] = filepath
                    self.search_results[name] = matching_sections
                    
            except Exception:
                continue
        
        return results
    
    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle search input changes"""
        if event.input.id == "search-input":
            self._filter_cheatsheets(event.value)
    
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle cheatsheet selection"""
        if event.item and hasattr(event.item, '_cheatsheet_filepath'):
            self.current_file = event.item._cheatsheet_filepath
            self._render_cheatsheet(event.item._cheatsheet_filepath)
        else:
            # Debug: Show what we got
            self.query_one("#status", Static).update(f"Debug: Selected item has no filepath attribute")
    
    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Handle cheatsheet highlighting (when navigating with arrow keys)"""
        if event.item and hasattr(event.item, '_cheatsheet_filepath'):
            # Update status to show which file would be selected
            self.query_one("#status", Static).update(
                f"Highlighted: {event.item._cheatsheet_name} | Press Enter to view"
            )
    
    def action_focus_search(self) -> None:
        """Focus the search input field."""
        self.query_one("#search-input", Input).focus()

    def action_toggle_dark(self) -> None:
        """Toggle between dark and light themes"""
        self.dark = not self.dark
        if self.dark:
            try:
                self.theme = "dracula"
            except Exception:
                self.theme = "dark"
        else:
            self.theme = "light"

def main():
    """Main entry point for the application"""
    import sys
    cheatsheets_dir = sys.argv[1] if len(sys.argv) > 1 else None
    app = CheatsheetManager(cheatsheets_dir)
    app.run()

if __name__ == "__main__":
    main()
