package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	fmt.Println("test")

	return (l1)
}

func main() {
	res := addTwoNumbers(
		&ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: &ListNode{}}}},
		&ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4, Next: &ListNode{}}}},
	)

	fmt.Println(res.Val, res.Next.Val, res.Next.Next.Val)

}
