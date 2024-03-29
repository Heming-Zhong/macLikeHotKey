# macLikeHotKey
A macOS-Like Key-Mapping config for Windows 10/11 based on autohotkey and sharpkeys.

## Usage & Features

note: this self-use keymapping is based on this repo <u>https://github.com/stroebjo/autohotkey-windows-mac-keyboard</u> and <u> in addition with some custom config and improvements. Changes below are included or to be included:

- [x] line start and line end using `CMD/WIN + Left` and `CMD/WIN + Right`

- [x] line delete using `CMD/WIN + BackSpace`

- [x] line selection using `CMD/WIN + SHIFT + Left` and `CMD/WIN + SHIFT + Left`

- [x] `CMD/WIN + F1-5` for custom app launchers

- [x] custom keys for vscode

- [x] using `ALT` for word-based cursor actions

- [x] `CMD/WIN + SHIFT + 5` for fast screen recording
  
About how to use it:
1. Install autohotkey and sharpkeys on target windows computer.

2. Download this project's source and load `ctrl_win_swap.skl` using sharpkeys and compile `keymapping.ahk` using autohotkey.
  
3. (Optional) Set up a customized log-in task to launch keymapping programs automatically. This can be done through Task Scheduler in Computer Management.
  
4. Done.
  
NOTE: ahk keymappings is recommended to run with administrator. Or it will not work with privileged softwares.

## Things you need to know

1. This is a self-use keymapping config. It works perfectly for **MY WIN10 COMPUTER**, but it may not work well on Other environment. 
2. Be that as it may, feel free to raise an issue.
3. custom app launchers launch apps with the paths on MY PC, so you might need to change the executable path to your own in order to make it work.
4. As mentioned above, it's a self-use script so it won't be 100% the same as the system keymappings on macOS. If you just don't like the customed part, feel free to fork and modify one of your own.
5. There might be a "pure mac-Like" version in the future.
6. Finally, any contribution are welcomed.

## Credits

Thanks to the authors of <u>https://github.com/stroebjo/autohotkey-windows-mac-keyboard</u>, which this repo is based on.

Also thanks to the authors of [autohotkey](https://www.autohotkey.com/), [sharpkeys](https://github.com/randyrants/sharpkeys) and [kinto](https://github.com/rbreaves/kinto). Their great contributions helped a lot to my little project.
