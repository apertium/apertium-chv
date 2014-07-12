cat wiki.yaml | grep "Сӑмах $1\"" > /tmp/$1-1.yaml
cat wiki.yaml | grep " $1<" > /tmp/$1-2.yaml
cat cap_yaml.txt /tmp/$1-1.yaml /tmp/$1-2.yaml > $1.yaml
