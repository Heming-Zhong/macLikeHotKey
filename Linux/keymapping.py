import re
from xkeysnail.transform import *

# ====================== Application Groups ====================== 

# Use the following for testing terminal keymaps
# terminals = [ "", ... ]
# xbindkeys -mk
terminals = [
    "alacritty",
    "cutefish-terminal",
    "deepin-terminal",
    "eterm",
    "gnome-terminal",
    "guake",
    "hyper",
    "io.elementary.terminal",
    "kinto-gui.py",
    "kitty",
    "Kgx",                      # GNOME Console terminal app
    "konsole",
    "lxterminal",
    "mate-terminal",
    "org.gnome.Console",
    "qterminal",
    "st",
    "sakura",
    "station",
    "tabby",
    "terminator",
    "termite",
    "tilda",
    "tilix",
    "urxvt",
    "xfce4-terminal",
    "xterm",
    "yakuake"
]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str('^'+x+'$') for x in terminals)

mscodes = ["code","vscodium"]
codeStr = "|".join(str('^'+x+'$') for x in mscodes)

sublimes   = ["Sublime_text","subl"]
sublimeStr = "|".join(str('^'+x+'$') for x in sublimes)

# Add remote desktop clients & VM software here
# Ideally we'd only exclude the client window,
# but that may not be easily done.
remotes = [
    "Gnome-boxes",
    "org.remmina.Remmina",
    "remmina",
    "qemu-system-.*",
    "qemu",
    "Spicy",
    "Virt-manager",
    "VirtualBox",
    "VirtualBox Machine",
    "xfreerdp",
    "Wfica",
    "Anydesk",
]
remotes = [client.casefold() for client in remotes]
remotesStr = "|".join(str('^'+x+'$') for x in remotes)

# Add remote desktop clients & VMs for no remapping
terminals.extend(remotes)
mscodes.extend(remotes)

# Use for browser specific hotkeys
browsers = [
    "Brave-browser",
    "Chromium",
    "Chromium-browser",
    "Discord",
    "Epiphany",
    "Firefox",
    "Firefox Developer Edition",
    "Navigator",
    "firefoxdeveloperedition",
    "Waterfox",
    "Google-chrome",
    "microsoft-edge",
    "microsoft-edge-dev",
    "org.deepin.browser",
]
browsers = [browser.casefold() for browser in browsers]
browserStr = "|".join(str('^'+x+'$') for x in browsers)

chromes = [
    "Brave-browser",
    "Chromium",
    "Chromium-browser",
    "Google-chrome",
    "microsoft-edge",
    "microsoft-edge-dev",
    "org.deepin.browser",
]
chromes = [chrome.casefold() for chrome in chromes]
chromeStr = "|".join(str('^'+x+'$') for x in chromes)

# edges = ["microsoft-edge-dev","microsoft-edge"]
# edges = [edge.casefold() for edge in edges]
# edgeStr = "|".join(str('^'+x+'$') for x in edges)

# ====================== Global key exchanges ======================

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    # 模仿macOS，使用Caplock进行输入法切换
    Key.CAPSLOCK: Key.RIGHT_SHIFT,   # Caps2lshift - Self Defined Input Method Switching

    # 模仿macOS，将cmd和ctrl进行对换
    Key.LEFT_META: Key.RIGHT_CTRL,  
    Key.LEFT_CTRL: Key.LEFT_META,   
    Key.RIGHT_META: Key.RIGHT_CTRL, 
    Key.RIGHT_CTRL: Key.RIGHT_META,
})

# ====================== Dolphin: Finder shortcuts ======================

define_keymap(re.compile("^dolphin$", re.IGNORECASE),{
    K("RC-KEY_2"):      K("C-KEY_3"),           # View as List (Detailed)
    K("RC-KEY_3"):      K("C-KEY_2"),           # View as List (Compact)
    ##########################################################################################
    ### "Open in new window" requires manually setting custom shortcut of Ctrl+Shift+o
    ### in Dolphin's keyboard shortcuts. There is no default shortcut set for this function.
    ##########################################################################################
    ### "Open in new tab" requires manually setting custom shortcut of Ctrl+Shift+o in
    ### Dolphin's keyboard shortcuts. There is no default shortcut set for this function.
    ##########################################################################################
    K("RC-Super-o"):    K("RC-Shift-o"),        # Open in new window (or new tab, user's choice, see above)
    K("RC-Shift-N"):    K("F10"),               # Create new folder
    K("RC-comma"):      K("RC-Shift-comma"),    # Open preferences dialog
},"Overrides for Dolphin - Finder Mods")

filemanagers = [
    "caja",
    "cutefish-filemanager",
    "dde-file-manager",
    "dolphin",
    "io.elementary.files",
    "nautilus",
    "nemo",
    "org.gnome.nautilus",
    "pcmanfm",
    "pcmanfm-qt",
    "spacefm",
    "thunar",
]
filemanagers = [filemanager.casefold() for filemanager in filemanagers]
filemanagerStr = "|".join(str('^'+x+'$') for x in filemanagers)

# Currently supported Linux file managers (file browsers):
#
# Caja File Browser (MATE file manager, fork of Nautilus)
# DDE File Manager (Deepin Linux file manager)
# Dolphin (KDE file manager)
# Nautilus (GNOME file manager, may be named "Files")
# Nemo (Cinnamon file manager, fork of Nautilus, may be named "Files")
# Pantheon Files (elementary OS file manager, may be named "Files")
# PCManFM (LXDE file manager)
# PCManFM-Qt (LXQt file manager)
# SpaceFM (Fork of PCManFM file manager)
# Thunar File Manager (Xfce file manager)
#
# Keybindings for general Linux file managers group:
define_keymap(re.compile(filemanagerStr, re.IGNORECASE),{
    ###########################################################################################################
    ###  Show Properties (Get Info) | Open Settings/Preferences | Show/Hide hidden files                    ###
    ###########################################################################################################
    K("RC-i"):                  K("Alt-Enter"),       # File properties dialog (Get Info)
    K("RC-comma"):              [K("Alt-E"),K("N")],  # Open preferences dialog
    K("RC-Shift-dot"):          K("RC-H"),          # Show/hide hidden files ("dot" files)
    ###########################################################################################################
    ###  Navigation                                                                                         ###
    ###########################################################################################################
    K("RC-Left_Brace"):         K("Alt-Left"),        # Go Back
    K("RC-Right_Brace"):        K("Alt-Right"),       # Go Forward
    K("RC-Left"):               K("Alt-Left"),        # Go Back
    K("RC-Right"):              K("Alt-Right"),       # Go Forward
    K("RC-Up"):                 K("Alt-Up"),          # Go Up dir
    # K("RC-Down"):               K("Alt-Down"),        # Go Down dir (only works on folders) [not universal]
    # K("RC-Down"):               K("RC-O"),          # Go Down dir (open folder/file) [not universal]
    K("RC-Down"):               K("Enter"),         # Go Down dir (open folder/file) [universal]
    K("RC-Shift-Left_Brace"):   K("C-Page_Up"),     # Go to prior tab
    K("RC-Shift-Right_Brace"):  K("C-Page_Down"),   # Go to next tab
    K("RC-Shift-Left"):         K("C-Page_Up"),     # Go to prior tab
    K("RC-Shift-Right"):        K("C-Page_Down"),   # Go to next tab
    ###########################################################################################################
    ###  Open in New Window | Move to Trash | Duplicate file/folder                                         ###
    ###########################################################################################################
    K("RC-Super-o"):            K("RC-Shift-o"),        # Open in new window (or tab, depends on FM setup) [not universal]
    K("RC-Backspace"):          K("Delete"),	        # Move to Trash (delete)
    # K("RC-D"):          [K("RC-C"),K("RC-V")],  # Duplicate file/folder (Copy, then Paste) [conflicts with "Add Bookmark"]
    ###########################################################################################################
    ###  To enable renaming files with the Enter key, uncomment the two keymapping lines just below this.   ###
    ###  Use Ctrl+Shift+Enter to escape or activate text fields such as "[F]ind" and "[L]ocation" fields.   ###
    ###########################################################################################################
    K("RC-Enter"):              K("F2"),            # Rename with Cmd+Enter key
},"General File Managers - Finder Mods")

# ====================== Edge: shortcuts on macOS ======================

# TODO

# ====================== Special overrides for terminals ======================
define_keymap(re.compile(termStr, re.IGNORECASE),{
    K("Alt-Backspace"):           K("Alt-Shift-Backspace"), # Wordwise delete word left of cursor in terminals
    K("Alt-Delete"):              [K("Esc"),K("d")],      # Wordwise delete word right of cursor in terminals
    K("RC-Backspace"):          K("C-u"),               # Wordwise delete line left of cursor in terminals
    K("RC-Delete"):             K("C-k"),               # Wordwise delete line right of cursor in terminals
},"Special overrides for terminals")


# ====================== General ======================
define_keymap(None, {
    # application
    K("RC-q"): K("Alt-F4"),                       # Quit app
    K("RC-m"): K("Super-h"),                      # minimize current window
    K("RC-Shift-m"): K("Super-d"),                # Show desktop

    # Wordwise
    K("RC-Left"): K("Home"),                      # Beginning of Line
    K("RC-Shift-Left"): K("Shift-Home"),          # Select all to Beginning of Line
    K("RC-Right"): K("End"),                      # End of Line
    K("RC-Shift-Right"): K("Shift-End"),          # Select all to End of Line
    K("RC-Up"): K("C-Home"),                      # Beginning of File
    K("RC-Shift-Up"): K("C-Shift-Home"),          # Select all to Beginning of File
    K("RC-Down"): K("C-End"),                     # End of File
    K("RC-Shift-Down"): K("C-Shift-End"),         # Select all to End of File
    K("Super-Backspace"): K("C-Backspace"),       # Delete Left Word of Cursor
    K("Super-Delete"): K("C-Delete"),             # Delete Right Word of Cursor
    K("Alt-Backspace"): K("C-Backspace"),         # Default not-chromebook
    K("RC-Backspace"): [K("Shift-Home"),K("Delete")],    # Delete Entire Line Left of Cursor
    K("Alt-Delete"): K("C-Delete"),               # Delete Right Word of Cursor
}, "General GUI")
