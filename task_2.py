from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(
                f"Illegal argument for findLongestCommonWord: strings = {strings} must be a list of strings"
            )

        for s in strings:
            if not isinstance(s, str) or not s:
                raise TypeError(
                    f"Illegal argument for findLongestCommonWord: strings = {strings} must be a list of strings"
                )

        [self.put(w, i) for i, w in enumerate(strings)]

        cmn = ''
        curr = self.root

        while len(curr.children) == 1:
            char, *_ = curr.children
            cmn += char
            curr = curr.children[char]

        return cmn


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
