#!/bin/bash

export PS2="| => "

alias cp='cp -iv'                           # Preferred 'cp' implementation
alias mv='mv -iv'                           # Preferred 'mv' implementation
alias mkdir='mkdir -pv'                     # Preferred 'mkdir' implementation
alias ll='ls --color=auto -FGlAhp'          # Preferred 'ls' implementation
alias less='less -FSRXc'                    # Preferred 'less' implementation
cd() { builtin cd "$@"; }                   # Always list directory contents upon 'cd'
alias cd..='cd ../'                         # Go back 1 directory level (for fast typers)
alias ..='cd ../'                           # Go back 1 directory level
alias ...='cd ../../'                       # Go back 2 directory levels
alias .3='cd ../../../'                     # Go back 3 directory levels
alias .4='cd ../../../../'                  # Go back 4 directory levels
alias .5='cd ../../../../../'               # Go back 5 directory levels
alias .6='cd ../../../../../../'            # Go back 6 directory levels
alias edit='subl'                           # edit:         Opens any file in sublime editor
alias ~="cd ~"                              # ~:            Go Home
alias c='clear'                             # c:            Clear terminal display
alias which='type -all'                     # which:        Find executables
alias path='echo -e ${PATH//:/\\n}'         # path:         Echo all executable Paths
alias show_options='shopt'                  # Show_options: display bash options settings
alias cic='set completion-ignore-case On'   # cic:          Make tab-completion case-insensitive
mcd () { mkdir -p "$1" && cd "$1"; }        # mcd:          Makes new Dir and jumps inside

pi_welcome () {
	let upSeconds="$(/usr/bin/cut -d. -f1 /proc/uptime)"
	let secs=$((${upSeconds}%60))
	let mins=$((${upSeconds}/60%60))
	let hours=$((${upSeconds}/3600%24))
	let days=$((${upSeconds}/86400))
	UPTIME=`printf "%d days, %02dh%02dm%02ds" "$days" "$hours" "$mins" "$secs"`

	# get the load averages
	read one five fifteen rest < /proc/loadavg

	echo "$(tput setaf 2)
	   .~~.   .~~.    `date +"%A, %e %B %Y, %X %Z"`
	  '. \ ' ' / .'   `uname -srmo`$(tput setaf 1)
	   .~ .~~~..~.    
	  : .~.'~'.~. :   Uptime.............: ${UPTIME}
	 ~ (   ) (   ) ~  Memory.............: `cat /proc/meminfo | grep MemFree | awk {'print $2'}`kB (Free) / `cat /proc/meminfo | grep MemTotal | awk {'print $2'}`kB (Total)
	( : '~'.~.'~' : ) Load Averages......: ${one}, ${five}, ${fifteen} (1, 5, 15 min)
	 ~ .~ (   ) ~. ~  Running Processes..: `ps ax | wc -l | tr -d " "`
	  (  : '~' :  )   CPU Temperature....: `/opt/vc/bin/vcgencmd measure_temp | cut -c 6-9 | awk '{ print $1 "°C" }'`
	   '~ .~~~. ~'    Free Disk Space....: `df -Ph | grep -E '^/dev/root' | awk '{ print $4 " of " $2 }'`
	       '~'  	  IP Addresses.......: `/sbin/ifconfig eth0 | /bin/grep "inet addr" | /usr/bin/cut -d ":" -f 2 | /usr/bin/cut -d " " -f 1` and `wget -q -O - http://icanhazip.com/ | tail`
	          	  Weather............: `curl -s "http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|PL|PL007|WARSZAWA|" | sed -n '/Currently:/ s/.*: \(.*\): \([0-9]*\)\([CF]\).*/\2°\3, \1/p'`
	$(tput sgr0)"
}

pi_cmds () {
	echo "$(cat /home/pi/dev/README.md)"
}


