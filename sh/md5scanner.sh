#/bin/bash
$MD5SUM = "25ce9982b3fc6e957bcfcebc66aa8605"
find . -type f -exec md5sum {} + | grep $MD5SUM > md5scanner.tmp
rm -rf `cat md5scanner.tmp | gawk -F"  " '{ print $2 }'`
