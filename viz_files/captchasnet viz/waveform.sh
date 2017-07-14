#!/bin/bash
echo "Creating Spectrogram!"

sox $1 -n spectrogram
sox $1 -n spectrogram -l -r -o "spectrogram_light.png"
sox $1 -n spectrogram -m -r -o "spectrogram_monochrome.png"

xdg-open spectrogram.png

echo "Creating waveform!"

sox $1 audio.dat
tail -n+3 audio.dat > audio_only.dat

gnuplot audio.gpi