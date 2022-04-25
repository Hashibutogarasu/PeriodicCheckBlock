import re

def supcious_match(str):
    #strの中から怪レい単語を探して結果をboolで返す
    #True:単語を発見に返す
    #False:単語が見つからなかった場合に返す
    match = r".*🔞|💕|♥|💖|💓|💚|💞|🖤|💜|💗|💙|💛|🎀|現金配布|副業|から成り上がり|[0-9]+万円を(プレゼント|配布)|秘書|ふぉろー|ふぉー|エロ|えろ|えち|ｴﾁ|えっちぃ|えっち|エッチ.*"
    return re.compile(match).search(str)


#matchの内容タイプするのきつい！