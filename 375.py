"""
The h-index is a metric used to measure the impact and productivity of a scientist or researcher.

A scientist has index h if h of their N papers have at least h citations each, and
the other N - h papers have no more than h citations each. If there are multiple possible values for h, the maximum value is used.

Given an array of natural numbers, with each value representing the number of citations of a researcher's paper,
return the h-index of that researcher.

For example, if the array was:

[4, 0, 0, 2, 3]
This means the researcher has 5 papers with 4, 1, 0, 2, and 3 citations respectively.
The h-index for this researcher is 2, since they have 2 papers with at least 2 citations and the remaining 3 papers have no more than 2 citations.

"""


def get_h_value(papers):
    sorted_papers = sorted(papers, reverse=True)
    max_cites = sorted_papers[0]
    for num in range(max_cites, 0, -1):
        h = num
        min_citations = 0
        max_citations = 0
        for paper in sorted_papers:
            if paper >= num:
                min_citations += 1

        if min_citations >= h:
            for paper in sorted_papers[h:]:
                if paper <= num:
                    max_citations += 1

            if max_citations == len(papers) - h:
                return num


def main():
    assert get_h_value([4, 0, 0, 2, 3]) == 2


if __name__ == '__main__':
    main()
