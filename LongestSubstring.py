'''
不重复子串
如果要是大于等于最近重复字符所在的位置的话，
那么一方面前面已经出现了这个重复字符
另一方面我们就需要是当前的重复子串的长度减1了
而那个start记录的值则是新的不重复子串开始的位置

整体思想总结：
用到的有 字典：字典的主要用途是记录每个字符出现的次数
		start变量：记录一个新的不重复子串的起始位置
		one_max：记录当前不重复子串的长度

主要思想就是：
我们从字符的第一个位置开始遍历，当出现新的字符时，就将其加到字典中去，其中key为字符值，value为字符出现的次数；
同时我们更新start值来记录新的不重复子串的起始位置
那么不重复子串的长度实际上就是 （当前的位置i）-start+1
也就是说 每次遍历的字符都要经历一次计算 子串长度。
'''
# 代码如下：

def lengthOfLongestSubstring(sefl, s):
	max_len = 0
	if s is None or len(s):
		return max_len
	str_dict = {}
	one_max = 0
	start = 0
	for i in range(len(s)):
		if s[i] in str_dict and str_dict[s[i]] >= start:
			start = str_dict[s[i] + !
		one_max = i - start +1
		str_dict[s[i]] = i
		max_len = max(max_len, one_max)
	return max_len

这一段代码是有问题的，但是我并不知道问题出在哪。其中我无法理解的就是为什么字典对应的value要 + 1