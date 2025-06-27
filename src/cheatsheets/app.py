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

class CheatsheetManager(App):
    """A Textual app for browsing cheatsheets"""
    
    CSS = (
        "#sidebar {\n"
        "    width: 30%;\n"
        "    border-right: solid $primary;\n"
        "}\n"
        "#content-panel {\n"
        "    width: 70%;\n"
        "    padding: 1;\n"
        "}\n"
        "#search-input {\n"
        "    margin: 1 0;\n"
        "}\n"
        ".list-item-label {\n"
        "    padding: 0 1;\n"
        "}\n"
        "#status {\n"
        "    height: 3;\n"
        "    background: $surface;\n"
        "    border-top: solid $primary;\n"
        "    padding: 1;\n"
        "}\n"
    )
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("ctrl+f", "focus_search", "Search"),
    ]
    
    # Reactive attributes
    current_file = reactive(None)
    search_term = reactive("")
    
    def __init__(self, cheatsheets_dir=None):
        super().__init__()
        self.cheatsheets_dir = Path(cheatsheets_dir or Path.home() / "cheatsheets")
        self.cheatsheets = {}
        self.filtered_cheatsheets = {}
        
    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header(show_clock=True)
        
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
            label_text = f"{i:2d}. {name.lower()}"
            label = Label(label_text, classes="list-item-label")
            list_item = ListItem(label)
            list_item._cheatsheet_name = name
            list_item._cheatsheet_filepath = filepath
            list_view.append(list_item)
    
    def _filter_cheatsheets(self, search_term: str):
        """Filter cheatsheets based on search term (name or number)"""
        if not search_term:
            self.filtered_cheatsheets = self.cheatsheets.copy()
        else:
            results = {}
            # Get a sorted list of all cheatsheets to associate numbers with them
            sorted_cheatsheets = sorted(self.cheatsheets.items())
            
            for i, (name, path) in enumerate(sorted_cheatsheets, 1):
                # Check if the search term is in the name (case-insensitive)
                name_match = search_term.lower() in name.lower()
                # Check if the search term is the number of the item in the list
                number_match = search_term == str(i)
                
                if name_match or number_match:
                    results[name] = path
            
            self.filtered_cheatsheets = results

        self._update_list()
        
        # Update status
        if search_term:
            count = len(self.filtered_cheatsheets)
            self.query_one("#status", Static).update(
                f"Search: '{search_term}' - {count} matches"
            )
        else:
            self.query_one("#status", Static).update(
                f"Found {len(self.cheatsheets)} cheatsheets | Use Ctrl+F to search"
            )
    
    def _render_cheatsheet(self, filepath):
        """Render markdown file in the content panel"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content_widget = self.query_one("#content", Markdown)
            content_widget.update(content)
            
            # Update status
            self.query_one("#status", Static).update(
                f"Viewing: {filepath.stem} | Press 'r' to refresh, 'q' to quit"
            )
            
        except FileNotFoundError:
            content_widget = self.query_one("#content", Markdown)
            content_widget.update(f"## Error: File '{filepath}' not found")
        except Exception as e:
            content_widget = self.query_one("#content", Markdown)
            content_widget.update(f"## Error reading file: {e}")
    
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

def main():
    """Main entry point for the application"""
    import sys
    cheatsheets_dir = sys.argv[1] if len(sys.argv) > 1 else None
    app = CheatsheetManager(cheatsheets_dir)
    app.run()

if __name__ == "__main__":
    main()
