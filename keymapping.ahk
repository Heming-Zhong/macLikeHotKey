;-----------------------------------------
; Mac keyboard to Windows Key Mappings
;=========================================

; --------------------------------------------------------------
; NOTES
; --------------------------------------------------------------
; ! = ALT
; ^ = CTRL
; + = SHIFT
; # = WIN
;
; Debug action snippet: MsgBox You pressed Control-A while Notepad is active.

#InstallKeybdHook
#SingleInstance force
SetTitleMatchMode 2
SendMode Input

; --------------------------------------------------------------
; Mac-like screenshots in Windows (requires Windows 10 Snip & Sketch)
; --------------------------------------------------------------

; Capture entire screen with CMD/WIN + SHIFT + 3
^+3::Send {PrintScreen}

; Capture portion of the screen with CMD/WIN + SHIFT + 4
^+4::Send #+{S}

; Screen recording with CMD/WIN + SHIFT + 5
^+5::Send #!g

; --------------------------------------------------------------
; media/function keys all mapped to the right option key
; --------------------------------------------------------------

F7::SendInput {Media_Prev}
F8::SendInput {Media_Play_Pause}
F9::SendInput {Media_Next}
F10::SendInput {Volume_Mute}
F11::SendInput {Volume_Down}
F12::SendInput {Volume_Up}

; swap left command/windows key with left alt
;LWin::LAlt
;LAlt::LWin ; add a semicolon in front of this line if you want to disable the windows key

; Remap Windows + Left OR Right to enable previous or next web page
; Use only if swapping left command/windows key with left alt
;Lwin & Left::Send, !{Left}
;Lwin & Right::Send, !{Right}

; F13-15, standard windows mapping
F13::SendInput {PrintScreen}
F14::SendInput {ScrollLock}
F15::SendInput {Pause}

; CMD/WIN + F1-8 custom app launchers, see http://www.autohotkey.com/docs/Tutorial.htm for usage info
; Section 1: frequently used apps
#F1::Run C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe    ; run VSCode to code
#F2::Run C:\Users\Dell\AppData\Local\Programs\Notion\Notion.exe             ; run Notion to take notes
#F3::Run %LocalAppData%\Microsoft\WindowsApps\wt.exe                        ; run Windows Terminal to use term
#F4::Run C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe       ; run Edge to surf the Internet

; Section 2: System related apps
#F5::Run C:\Windows\system32\taskmgr.exe    ; run task manager to monitor and kill proc


; --------------------------------------------------------------
; OS X system shortcuts
; --------------------------------------------------------------

; Close windows (cmd + q to Alt + F4)
^q::Send !{F4}

; Minimize active window
^m::WinMinimize, A

; Minimize all
!^m::WinMinimizeAll

; Remap Windows + Tab to Alt + Tab.
Lwin & Tab::AltTab

; Desktop switch shortcuts
#Left::Send #^{Left}
#Right::Send #^{Right}

; --------------------------------------------------------------
; macOS keyboard mappings for special chars
; --------------------------------------------------------------

; Map Alt + L to @
!l::SendInput {@}

; Map Alt + N to \
+!7::SendInput {\}

; Map Alt + N to ©
!g::SendInput {©}

; Map Alt + o to ø
!o::SendInput {ø}

; Map Alt + 5 to [
!5::SendInput {[}

; Map Alt + 6 to ]
!6::SendInput {]}

; Map Alt + E to €
!e::SendInput {€}

; Map Alt + - to –
!-::SendInput {–}

; Map Alt + 8 to {
!8::SendInput {{}

; Map Alt + 9 to }
!9::SendInput {}}

; Map Alt + - to ±
!+::SendInput {±}

; Map Alt + R to ®
!r::SendInput {®}

; Map Alt + N to |
!7::SendInput {|}

; Map Alt + W to ∑
!w::SendInput {∑}

; Map Alt + N to ~
!n::SendInput {~}

; Map Alt + 3 to #
!3::SendInput {#}



; --------------------------------------------------------------
; Custom mappings for special chars
; --------------------------------------------------------------

;#ö::SendInput {[} 
;#ä::SendInput {]} 

;^ö::SendInput {{} 
;^ä::SendInput {}} 

; --------------------------------------------------------------
; Cursor actions in OS X
; --------------------------------------------------------------

; move the cursor to the line start or end
^Left::Send, {Home}
^Right::Send, {End}

; select the cursor to the line start or end
^+Left::Send +{Home}
^+Right::Send +{End}

; move the cursor to the page top or bottom
^Up::Send, ^{Home}
^Down::Send, ^{End}

; select the content to the top or bottom
^+Up::Send, ^+{Home}
^+Down::Send, ^+{End}

; delete to the line start
$^BackSpace::Send +{Home}{Delete}

; change word select to alt, including delete
!Left::Send ^{Left}
!Right::Send ^{Right}
!+Left::Send ^+{Left}
!+Right::Send ^+{Right}
!BackSpace::Send ^{BackSpace}

; --------------------------------------------------------------
; Application specific
; --------------------------------------------------------------

; New Edge
#IfWinActive, ahk_exe msedge.exe

; Show Web Developer Tools with cmd + alt + i
^!i::Send {F12}

; Show source code with cmd + alt + u
^!u::Send ^u

; undo tab close
^z::Send ^!t

#IfWinActive

; Visual Studio Code
#IfWinActive, ahk_exe Code.exe

; NOTE: Need to set terminal:clear to ctrl+k first
#k::Send ^k

#IfWinActive

#IfWinActive ahk_class CabinetWClass ahk_exe explorer.exe

^i::Send !{Enter}           ; Cmd+i: Get Info
^BackSpace::Send {Delete}   ; Cmd+Backspace: send to trash
^d::return,                 ; block default ctrl+d shortcut
^r::Send {F5}               ; Cmd+r: Refresh
$Enter:: 			        ; Use Enter key to rename (F2), unless focus is inside a text input field. TODO: resolve conflicts with monitor brightness
ControlGetFocus, fc, A
If fc contains Edit,Search,Notify,Windows.UI.Core.CoreWindow1,SysTreeView321
    Send {Enter}
Else Send {F2}
Return

#IfWinActive
; --------------------------------------------------------------
; mouse/trackpad related actions
; --------------------------------------------------------------
