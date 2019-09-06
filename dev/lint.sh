
n_fail=`bash dev/check-multichars.sh | tee /tmp/lint-fail.0 | wc -l`;
ex_fail=`head -3 /tmp/lint-fail.0 | sed 's/ //g' | cut -f1 -d'!' | tr '\n' '\t'`;
echo -e "$n_fail\tmissing multi\t$ex_fail";

n_fail=`cat apertium-chv.chv.lexc | grep '^\([а-я][a-z]\|[a-z][а-я]\)\+:' | tee /tmp/lint-fail.1 | wc -l`;
ex_fail=`head -3 /tmp/lint-fail.1 | tr '\n' '\t'`;
echo -e "$n_fail\tmixed script\t$ex_fail"

rm /tmp/lint-fail.*
