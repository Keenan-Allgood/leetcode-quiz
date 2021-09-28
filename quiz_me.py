import random


class Quiz:
    array = {
        1: "https://leetcode.com/problems/two-sum/",
        11: "https://leetcode.com/problems/container-with-most-water/",
        15: "https://leetcode.com/problems/3sum/",
        53: "https://leetcode.com/problems/maximum-subarray/",
        56: "https://leetcode.com/problems/merge-intervals/",
        88: "https://leetcode.com/problems/merge-sorted-array/",
        121: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        125: "https://leetcode.com/problems/valid-palindrome/",
        152: "https://leetcode.com/problems/maximum-product-subarray/",
        217: "https://leetcode.com/problems/contains-duplicate/",
        238: "https://leetcode.com/problems/product-of-array-except-self/",
        242: "https://leetcode.com/problems/valid-anagram/",
        252: "https://leetcode.com/problems/meeting-rooms/",
        253: "https://leetcode.com/problems/meeting-rooms-ii/",
        283: "https://leetcode.com/problems/move-zeroes/",
        953: "https://leetcode.com/problems/verifying-an-alien-dictionary/",
        1089: "https://leetcode.com/problems/duplicate-zeros/"
    }

    linked_list = {
        19: "https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
        21: "https://leetcode.com/problems/merge-two-sorted-lists/",
        23: "https://leetcode.com/problems/merge-k-sorted-lists/",
        141: "https://leetcode.com/problems/linked-list-cycle/",
        143: "https://leetcode.com/problems/reorder-list/",
        206: "https://leetcode.com/problems/reverse-linked-list/"
    }

    matrix = {
        48: "https://leetcode.com/problems/rotate-image/",
        54: "https://leetcode.com/problems/spiral-matrix/",
        73: "https://leetcode.com/problems/set-matrix-zeroes/",
        79: "https://leetcode.com/problems/word-search/",
        36: "https://leetcode.com/problems/valid-sudoku/submissions/"
    }

    binary_tree = {

    }

    binary_search_tree = {

    }

    binary_search = {
        33: "https://leetcode.com/problems/search-in-rotated-sorted-array/",
        153: "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
        704: "https://leetcode.com/problems/binary-search/"
    }

    heap = {
        23: "https://leetcode.com/problems/merge-k-sorted-lists/",
        295: "https://leetcode.com/problems/find-median-from-data-stream/",
        347: "https://leetcode.com/problems/top-k-frequent-elements/"
    }

    intervals = {
        56: "https://leetcode.com/problems/merge-intervals/",
        57: "https://leetcode.com/problems/insert-interval/",
        252: "https://leetcode.com/problems/meeting-rooms/",
        253: "https://leetcode.com/problems/meeting-rooms-ii/",
        435: "https://leetcode.com/problems/non-overlapping-intervals/"
    }

    randoms = {

    }

    graph = {

    }

    back_tracking = {

    }

    sorting = {

    }

    strings = {
        3: "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        5: "https://leetcode.com/problems/longest-palindromic-substring/",
        8: "https://leetcode.com/problems/string-to-integer-atoi/",
        20: "https://leetcode.com/problems/valid-parentheses/",
        28: "https://leetcode.com/problems/implement-strstr/",
        49: "https://leetcode.com/problems/group-anagrams/",
        76: "https://leetcode.com/problems/minimum-window-substring/",
        151: "https://leetcode.com/problems/reverse-words-in-a-string/",
        186: "https://leetcode.com/problems/reverse-words-in-a-string-ii/",
        271: "https://leetcode.com/problems/encode-and-decode-strings/",
        344: "https://leetcode.com/problems/reverse-string/",
        387: "https://leetcode.com/problems/first-unique-character-in-a-string/",
        557: "https://leetcode.com/problems/reverse-words-in-a-string-iii/",
        647: "https://leetcode.com/problems/palindromic-substrings/"
    }

    options = [
        array,
        linked_list,
        matrix,
        binary_tree,
        binary_search_tree,
        intervals,
        randoms,
        graph,
        back_tracking,
        sorting,
        strings,
        binary_search,
        heap
    ]

    def pick_a_random_problem(self, disregard=[]):
        disregard_set = set()
        exclude_options = set()

        for i in disregard:
            if i not in disregard_set:
                disregard_set.add(i)

        option_excluded = True
        random_option = None
        keys = []

        while option_excluded:
            random_option_key = random.randint(0, len(self.options) - 1)
            random_option = self.options[random_option_key]
            keys = list(random_option.keys())

            if random_option_key not in exclude_options:
                for i in keys:
                    if i not in disregard_set:
                        option_excluded = False

                if option_excluded:
                    exclude_options.add(random_option_key)

        random_question_key = keys[random.randint(0, len(keys) - 1)]

        while random_question_key in disregard_set:
            random_question_key = keys[random.randint(0, len(keys) - 1)]

        print(str(random_question_key) + ": " + random_option[random_question_key])


q = Quiz()

session = []
q.pick_a_random_problem(session)