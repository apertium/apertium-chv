# txuvaix

## Stem classes

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

## Examples and assignment rules

* "Chuvash" words

* "Russian" words
  * Terminated in stressed vowel
    * Terminated in stressed я
      * тухья:тухья N ;
    * Terminated in stressed о
      * пальто:пальто N ;
      * звено:звено N ;
    * Terminated in stressed е
      * шоссе:шоссе N ;
    * Terminated in stressed и
      * такси:такси N-INFORMACI ;
  * Terminated in unstressed vowel
    * Terminated in unstressed я
      * аллея:алле%{й%}я N ;
      * стихия:стихи%{й%}я N ;
    * Terminated in unstressed а
      * литература:литератур%{а%} N ;
    * Terminated in unstressed о
      * барокко:барокк%{о%} N ;
      * министерство:министерств%{о%} N ;
    * Terminated in unstressed е
      * кофе:коф%{е%} N ;
      * платье:плать%{е%} N ;
      * училище:училищ%{е%} N ;
    * Terminated in unstressed и
      * информаци:информаци N-INFORMACI ;

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





