#!/bin/bash
case "$variable" in 
abc) echo "\$variable = abc" ;;
xyz) echo "\$cariable = xyz";;
esac
#!/bin/bash
echo hello; echo there
if [ -x "$filename" ]; then 
	echo "File $filename exists."; cp $filename $filename.bak
else 
	echo "File $filename not found."; touch $filename
fi;echo "File test complete."
