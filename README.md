# Simple-SFlock-Launcher

대상 파일의 파일 포맷을 인식하는 파이썬 모듈 sflock2 를 실행하는 간단한 파이썬 코드.

# Install

## Ubuntu / Debian
```
$ sudo apt-get install p7zip-full rar unace-nonfree cabextract lzip libjpeg8-dev zlib1g-dev zpaq gnupg
$ pip install SFlock2
```

## Windows
```
> pip install SFlock2
> pip install python-magic-bin
```

# Usage

```
usage: run_sflock.py [-h] --input INPUT

Simple sflock launcher.

options:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        input file path
```

# Example
```
> python .\run_sflock.py --input .\test
[-] Result
.\test\calc.exe:exe
.\test\index.js:js
```
