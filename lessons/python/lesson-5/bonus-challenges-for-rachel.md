## More Problems for Rachel

### Warmup

The following 3 you can do with a regular string accumulator pattern:

1. Given a phrase, generate the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
of the phrase (ROT13)--- don't look for the answer.
2. Given a phrase, reverse each of its characters.
3. Given a phrase, remove all its vowels.

### Super Duper Challenge

The user can input tags like this:

```
The <caesar|quick brown fox> <reverse|jumps> over the <novowels|lazy dog>.
```

And it would generate this string:

```
The xbpjr iyvdu mve spmuj over the lzy dg.
```

Explanation:

A tag has this form: `<TAG_NAME|TEXT>`. The `TAG_NAME` can be one of:
"caesar", "reverse", and "novowels", and each of them performs the following
to the TEXT contained within the tag:

* caesar - converts TEXT to its Caesar Cipher
* reverse - reverses TEXT
* novowels - removes all vowes from TEXT.

More examples:

```
My <caesar|mama> <novowels|always said>, <caesar|'Life is like a box of chocolates>. You never know <reverse|what you're gonna get>.
```

```
My znzn lwys sd, 'yvsr vf yvxr n obk bs pubpbyngrf. You never know teg annog er'uoy tahw.
```
