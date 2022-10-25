from twttr import shorten
def test_shorten():
    # test_cases = {"twitter":"twttr", "subhashini":"sbhshn", "morning":"mrnng", "afternoon":"ftrnn", "night":"nght", "-s":"-s"}
    # for k,v in test_cases:
    #     assert shorten(k) == v
    assert shorten("twitter") == "twttr"
    assert shorten("subhashini") == "sbhshn"
    assert shorten("morning") == "mrnng"