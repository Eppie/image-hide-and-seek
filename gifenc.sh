#!/bin/bash

# sh gifenc.sh -i input.mp4 -o output.gif

# defaults
palette="/tmp/palette.png" #location of temporary palette file
fps=24
verbose="-v verbose"
filters=

#usage and parameter assembly
function usage
{
	echo "Usage: gifenc.sh -i input.mp4 -o output.gif [-f 24] [-w 1024] [-h 768]"
	echo ""
	echo "-i | --input   input filename"
	echo "-o | --output  output filename (optional)"
	echo "-f | --fps     framerate in fps (optional; default=24)"
	echo "-w | --width   picture width (optional)"
	echo "-h | --height  picture height (optional; if not present"
	echo "               output will be scaled proportionally)"
	echo "--help         Outputs this help"
	return
}

function parameters
{
	filters="fps=$fps"

	if [[ ! -z $width ]]; then
		if [[ ! -z $height ]]; then
			filters+=",scale=$width:$height"
		else
			filters+=",scale=$width:-1"
		fi
		filters+=":flags=lanczos"
	fi
}

while [[ "$1" != "" ]]; do
	case $1 in
		-i | --input )
			shift
			fileinput=$1
			;;
		-o | --output )
			shift
			fileoutput=$1
			;;
		-f | --fps )
			shift
			fps=$1
			;;
		-w | --width )
			shift
			width=$1
			;;
		-h | --height )
			shift
			height=$1
			;;
		--help )
			usage
			exit 1
			;;
		* )
			usage
			exit 1
	esac
	shift
done

if [[ -z $fileinput ]]; then
	usage
	echo
	echo "Error: No file input present."
	exit 1
fi

# when no file output is present, use same name as input
if [[ -z $fileoutput ]]; then
	fileoutput="${fileinput%.*}.gif"
fi

parameters

ffmpeg $verbose -i "$fileinput" -vf "$filters,palettegen" -y $palette
ffmpeg $verbose -i "$fileinput" -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y "$fileoutput"
