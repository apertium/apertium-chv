
head=`grep -nH 'LEXICON Root' apertium-chv.chv.lexc  | cut -f2 -d':'`

for tag in `cat apertium-chv.chv.lexc | grep -o '%<[^>]\+%>' | sort -u`;  do
	found=`head -n $head apertium-chv.chv.lexc | grep "$tag" | wc -l`
	if [[ $found -eq 0 ]]; then
		echo "$tag                         !";
	fi
done

for tag in `cat apertium-chv.chv.lexc | grep -o '%{[^}]\+%}' | sort -u`;  do
	found=`head -n $head apertium-chv.chv.lexc | grep "$tag" | wc -l`
	if [[ $found -eq 0 ]]; then
		echo "$tag                         !";
	fi
done
