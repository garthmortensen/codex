# tmux.md

## About
**Name:** tmux (stands for 'terminal multiplexer', describing its ability to split and manage multiple terminal sessions in one window)

**Created:** Released in 2007 by Nicholas Marriott, tmux was created to let users manage multiple terminal sessions from a single window. Its purpose is to allow splitting, detaching, and reattaching terminal sessions for better productivity.

**Similar Technologies:** GNU Screen, byobu, dvtm, terminator, tilix

**Plain Language Definition:**
tmux lets you split your terminal into multiple panes and keep your work running even if you disconnect, making multitasking in the terminal much easier.

---

## Sessions

- `tmux new -s <name>`: Start a new session.
- `tmux ls`: List all sessions.
- `tmux attach -t <name>`: Attach to a named session.
- `tmux kill-session -t <name>`: Kill a named session.
- `tmux kill-server`: Kill the tmux server and all sessions.

## Windows (Tabs)

- `Ctrl+b c`: Create a new window.
- `Ctrl+b ,`: Rename the current window.
- `Ctrl+b n`: Move to the next window.
- `Ctrl+b p`: Move to the previous window.
- `Ctrl+b [0-9]`: Move to a specific window by number.
- `Ctrl+b w`: List all windows.
- `Ctrl+b &`: Kill the current window.
- `Ctrl+b f`: Find a window by name.

## Panes (Splits)

- `Ctrl+b %`: Split the current pane vertically.
- `Ctrl+b "`: Split the current pane horizontally.
- `Ctrl+b <arrow_key>`: Move between panes.
- `Ctrl+b z`: Toggle pane zoom (maximize/minimize).
- `Ctrl+b x`: Close (kill) the current pane.
- `Ctrl+b !`: Break the current pane into a new window.
- `Ctrl+b q`: Show pane numbers.
- `Ctrl+b o`: Toggle between panes.
- `Ctrl+b ;`: Go to the last active pane.
- `Ctrl+b {` / `Ctrl+b }`: Swap panes.

## Navigation

- `Ctrl+b <arrow_key>`: Move between panes.
- `Ctrl+b Ctrl+<arrow_key>`: Resize pane in the arrow key direction.
- `Ctrl+b Alt+<arrow_key>`: Resize pane by 5 cells in the arrow key direction.
- `Ctrl+b :resize-pane -L 10`: Resize the current pane 10 cells to the left.
- `Ctrl+b :resize-pane -R 10`: Resize the current pane 10 cells to the right.
- `Ctrl+b :resize-pane -U 5`: Resize the current pane 5 cells up.
- `Ctrl+b :resize-pane -D 5`: Resize the current pane 5 cells down.

## Copy Mode

- `Ctrl+b [`: Enter copy mode.
- `Space`: Start selection.
- `Enter`: Copy the selection.
- `q`: Quit copy mode.
- `v`: Begin selection.
- `y`: Copy the selection.

## Configuration

Your `tmux` configuration is stored in `~/.tmux.conf`. Here are some common settings:

```tmux
# Set a new prefix key
set-option -g prefix C-a
unbind-key C-b
bind-key C-a send-prefix

# Enable mouse support
set -g mouse on

# Set the default terminal mode
set -g default-terminal "screen-256color"

# Enable 256 colors
set -g terminal-overrides 'xterm*:colors=256'

# Set the history limit
set -g history-limit 10000

# Reload config
bind r source-file ~/.tmux.conf \; display "Config reloaded!"
```

## Pro Tips

- Hold Shift to select text with the mouse.
- `prefix + prefix` sends a literal `Ctrl+b`.
- Use `~/.tmux.conf` for custom configuration.
- `prefix :source-file ~/.tmux.conf` to reload the configuration.
