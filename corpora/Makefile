all: puupankki/puupankki.chv.conllu

cvorg-kaleidoskop.conllu: ../apertium-chv.chv.udx cvorg-kaleidoskop.dep cvorg-kaleidoskop.seg
	python3 ../scripts/conllise.py ../apertium-chv.chv.udx cvorg-kaleidoskop.dep cvorg-kaleidoskop.seg > $@

puupankki/puupankki.chv.conllu: cvorg-kaleidoskop.conllu 
	cat cvorg-kaleidoskop.conllu  > $@
	@cat puupankki/puupankki.chv.conllu | grep -P '^[0-9]\t' | wc -l
	@cat puupankki/puupankki.chv.conllu | grep 'sent_id' | wc -l

clean:
	rm *.conllu puupankki/puupankki.chv.conllu
