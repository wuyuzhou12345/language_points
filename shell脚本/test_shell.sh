#/bin/bash
Main(){
	path="/Users/luying/Downloads/apache-maven-3.5.2"
	files=`find $path -type f -size +1024k`
	for file in $files
	do
		echo $file
	done

	list="where are you from"
	echo ${#list}
	for i in $list;
	do
		echo "$i is ok";
	done

	echo $0
	echo $#
	echo $1
}

Main $@