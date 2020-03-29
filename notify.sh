# Get first header
message="https://www.npr.org/2020/03/29/823130995/sunday-puzzle-silent-anagrams"
content=$(curl -N https://www.npr.org/series/4473090/sunday-puzzle | iconv | grep -m 1 "class=\"title\"")
IFS="\""
read -ra ADDR <<< $content
# for i in ${ADDR[*]}
#   do # access each element of array
#     echo $i
#   done
echo ${ADDR[3]} > temp
echo "$message" > temp1
# newest=${ADDR[3]}
# $DIFF=$(diff temp temp1)
diff -u temp temp1
ret=$?
# if ["$(diff -u temp temp1)" != ""]
if [[ $ret -eq 0 ]];
then
    echo The directory was modified
    diff temp temp1
fi
# rm temp
# rm temp1
