/**
 * 优先级队列
 * 
 * 二叉堆的结构 Bianry heap
 * 利用数组结构实现完全二叉树
 * 
 * 特性：
 * 数组里的第一个元素拥有最高级别array[0]
 * 给定一个下标i，那么对于元素array[i]而言
 * 父节点对应的元素下标是(i-1) / 2
 * 左侧子节点对应的元素下标是2*i + 1
 * 右侧子节点对应的元素下标是2*i + 2
 * 数组中每个元素的优先级都必须要高于它两侧的子节点
 * 
 * 基本操作：
 * 向上筛选 O(logk ：添加新数据
 * 向下筛选 O(logk) ： 取出堆顶元素
 * 
 * 优先队列的初始化：（n个数据）
 * 误区：每加入一个数据，都要加入堆顶，则复杂度为O(nlogn)
 * 实际上，二叉树的大小是从一逐渐增长到n的，所以整个算法的复杂度为O(n)
 * 
 * 
 */