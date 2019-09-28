# Chuvash

## Stem classes

### Nouns

* `N-RADIO`: 
  * (Russian) loanwords ending in -о with underlying {в}
  * The final -о does not reduce 
  * The {в} only appears in the third person possessive forms
  * Second person singular is радю not \*радию/\*радиу

* `N-TU`:
  * Words with an underlying {в}
  * Stem vowel reduces before some suffixes, e.g. ту--тӑва

* `N-SUPĂN`: 
  * Words which have a locative in -рA in addition to -тA.
  * Words which have an ablative in -рAн in addition to -тAн.

* `N-VLAŞ`: 
  * Two nominative stems, -ҫ and -сть
  * Oblique is always -ҫ

* `N-ĔŞ`: 
  * Extra 2nd person singular + dative in -нA in addition to -U(н)-нA

* `N-ANNE`: 
  * The word "анне" *mother*
  * Irregular possessive forms

* `N-ATTE`: 
  * The word "атте" *father*
  * Irregular possessive forms

* `N-ATTEANNE`: 
  * The word "атте-анне" *parents*
  * Irregular possessive forms

### Adjectives

* `A1`: 
  * Adjectives which do not permit substantivisation or comparison
* `A2`: 
  * Adjectives which permit both substantivisation and comparison and do not end in -р, -л, -н, -и, -у, -ӳ
* `A2-R`: 
  * Adjectives which permit both substantivisation and comparison and end in -р
* `A2-LN`: 
  * Adjectives which permit both substantivisation and comparison and end in -л, -н
* `A2-IUÜ`: 
  * Adjectives which permit both substantivisation and comparison and end in -и, -у, -ӳ

### Adverbs

* `ADV1`: 
  * Adverbs which do not permit comparison
* `ADV2`: 
  * Adverbs which permit comparison

### Verbs

## Examples and assignment rules

### Nouns

* Terminated in consonant
  * "Chuvash" words
    * "Chuvash" words terminated in л, ль, н, нь
      * супӑнь:супӑнь N-SUPĂN ;
    * "Chuvash" words terminated in consonant, except л, ль, н, нь
      * ӑвӑс:ӑвӑс N-ĔŞ ;
  * "Russian" words
    * "Russian" words terminated in ль or нь
      * автомагистраль:автомагистраль N-SUPĂN ;
    * "Russian" words terminated in сть
      * область:обла N-VLAÇ ;
    * "Russian" words terminated in ь, but not in ль, нь or сть (only a front vowel can follow)
      * тетрадь:тетрадь N-ĔŞ ; 
    * "Russian" words terminated in е, э or и + л or н (only a back vowel can follow)
      * бензин:бензин N-BENZIN ;
    * "Russian" words terminated in а, о, у or ы + л or н (N-SUPĂN and N-BENZIN are synonyms in this case)
      * район:район N-BENZIN ;
    * "Russian" words terminated in ей (both front and back vowel can follow)
      * музей:музей N-MUZEY ;
    * "Russian" words terminated in е, э or и + consonant, but not й, л, н (only a back vowel can follow)
      * проспект:проспект N-IZM ;
    * "Russian" words terminated in а, о, у or ы + consonant , but not й, л, н (N-ĔŞ and N-BENZIN are synonyms in this case)
      * класс:класс N-ĔŞ ;
* Terminated in Vowel + Consonant + ӑ or ӗ (stressed or not)
  * Terminated in Vowel + Consonant + ӑ (and a few more cases of consonant duplication)
    * пулӑ:пул%{ː%}ӑ N ;
    * пуртӑ:пурт%{ː%}ӑ N ;
  * Terminated in Vowel + Consonant + ӗ
    * кӳлӗ:кӳл%{ː%}ӗ N ;
* Terminated in stressed vowel
  * Terminated in stressed и
    * такси:такси N-INFORMACI ;
  * "Chuvash" words terminated in stressed у, ӳ
    * ӑмӑрту:ӑмӑрту N-TU ;
  * The cases of "Russian" words terminated in stressed у are extremely rare and uncertain (e.g. кенгуру)
  * Terminated in stressed vowel except и, у, ӳ
    * тухья:тухья N ;
    * пальто:пальто N ;
    * звено:звено N ;
    * шоссе:шоссе N ;
* "Russian" nouns terminated in unstressed vowel
    * Terminated in unstressed а
      * литература:литератур%{а%} N ;
    * Terminated in unstressed я
      * аллея:алле%{й%}я N ;
      * стихия:стихи%{й%}я N ;
    * Terminated in unstressed е
      * кофе:коф%{е%} N ;
      * платье:плать%{е%} N ;
      * училище:училищ%{е%} N ;
    * Terminated in unstressed и
      * информаци:информаци N-INFORMACI ;
    * Terminated in unstressed о
      * барокко:барокк%{о%} N ;
      * министерство:министерств%{о%} N ;
    * The cases of unstressed -у are extremely rare and uncertain (e.g. урду, ноу-хоу)
* Compound nouns finishing in izafet (they do not accept a possessive suffix after the lemma)
  * нумайлӑх% теорийӗ:нумайлӑх% теорийӗ N-COMPOUND-PX ;
  * операци% системи:операци% системи N-COMPOUND-PX ;

### Verbs
Three verbal terminations must have an epenthetic "diacritic" at the end of the stem:
  * и
      * ҫи:ҫи%{й%} V-TV ;
  * у
      * ту:ту%{в%} V-TV ;
  * ӳ
      * тӳ:тӳ%{в%} V-TD ;

### Toponyms
Toponyms function like nouns, so there should be, as a rule, the same number of cases there is for nouns. But not all terminations are found
* Terminated in vowel
  * Terminated in и
    * Киргизи:Киргизи NP-TOP-UDMURTI ;
  * Terminated in ӑ, ӗ preceeded by more than one consonant
    * Шӑмӑршӑ:Шӑмӑршӑ NP-TOP ;
  * Terminated in ӑ, ӗ preceeded by one consonant
    * Мӑн% Вылӑ:Мӑн% Выл%{ː%}ӑ NP-TOP;
  * Terminated in unstressed а
    * Палестина:Палестин%{а%} NP-TOP ;
  * Terminated in unstressed о
    * Сан-Марино:Сан-Марин%{о%} NP-TOP ;
  * Terminated in unstressed я
    * Корея:Коре%{й%}я NP-TOP ;
  * Terminated in stressed а, е
    * Махачкала:Махачкала NP-TOP;
  * Terminated in stressed у, ӳ
    * Ҫӗрпӳ:Ҫӗрпӳ%{в%} NP-TOP;
  * Other cases are dubious, and probably need another word like "island" and/or maybe "land", e.g.
    * Науру:Науру NP-TOP ;
    * Палау:Палау NP-TOP ;
    * Перу:Перу NP-TOP ;
    * Ниуэ:Ниуэ NP-TOP ;
* Terminated in consonant
  * "Russian" toponyms terminated in е, э or и + л or н (only a back vowel can follow)
    * Бенин:Бенин NP-TOP-BERLIN ;
  * "Russian" toponyms terminated in а, о, у or ы + л or н (NP-TOP-LN and NP-TOP-BERLIN are synonyms in this case)
    * Урус-Мартан:Урус-Мартан NP-TOP-LN ;
  * "Russian" toponyms terminated in е, э or и + consonant but not л or н (only a back vowel can follow)
    * Архангельск:Архангельск NP-TOP-SK ;
    * Кипр:Кипр NP-TOP-SK ;
  * "Russian" toponyms terminated in а, о, у or ы + consonant but not л or н (NP-TOP-SK and N-BENZIN are synonyms in this case)
    * Барбадос:Барбадос NP-TOP-SK ;
  * Toponyms terminated in ль or нь
    * Тюмень:Тюмень NP-TOP-LN ;
  * Toponyms terminated in ий
    * Первомайский:Первомайски NP-TOP-IJ ;
  * Toponyms terminated in consonants except л, ль, н, нь, ий
    * Ҫӗнӗ% Шупашкар:Ҫӗнӗ% Шупашкар NP-TOP ;
* Plural toponyms 
  * Филиппинсем:Филиппинсем NP-TOP-PL ;
* Compound toponyms finishing in izafet, including the ones finish in касси and the like (they do not accept a possessive suffix after the lemma)
  * Совет% Союзӗ:Совет% Союзӗ NP-TOP-PX ;
  * Хыркасси:Хыркасси NP-TOP-PX ;

## Archiphonemes 

## "Diacritics" 

* `{ь}` — force front harmony
* `{ъ}` — force back harmony
* `{☭}` — loanword phonology

### 3rd person possessive 

Underlying form: `>{и}{н}`

Rules: 

* `{и}` deletes stem vowel and surfaces as и
* `{и}` surfaces as ӗ after consonant
* Final consonant clusters are simplified -лл → -л, -сс → -с

# TODO 

Final vowel in платье does not reduce

```
+	платье<n><px1sg><nom>		платьем	
+	училище<n><px1sg><nom>		училищӗм
```

Epenthetic `{н}` does not appear after 2nd person possessive

```
-	анне<n><px2sg><loc>	анн{ь}>{U}{н}>{T}{A}	аннӳре	!= аннӳнте	
-	анне<n><px2sg><abl>	анн{ь}>{U}{н}>{T}{A}н	аннӳрен	!= аннӳнтен
```

Final unstressed vowels in Russian loanwords should probably be dealt 
with via a special symbol instead of by a separate archiphoneme for each
vowel.

The reason why it has been done with a separate archiphoneme so far is 
for vowel harmony purposes. Deleted surface vowels do not effect vowel
harmony rules, but in the case of these kinds they should, e.g. 

```
-	министерство<n><gen>	министерство{↓}>{Ă}н	министерствӑн	министерствӗн

```

If the surface о /ă/ is deleted then the ord gets front harmony from the stressed /e/.

One possibility is to mark the Russian loans with the `{☭}` and with a symbol
for stressed (or unstressed) vowel and then have the phonology treat these 
differently. e.g. either:

* `министерство{↓}{☭}>{Ă}н`, `пальто{☭}>{Ă}н`, or:
* `министерство{☭}>{Ă}н`, `пальто%{'%}{☭}>{Ă}н`

