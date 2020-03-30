package main

import "fmt"

// Definition for singly-linked list
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	dummyHead := &ListNode{Val: 0, Next: nil}
	var prevlist *ListNode

	//keeps track of carries
	carry := 0
	for l1 != nil || l2 != nil {

		var value1, value2, sum int

		if l1 != nil {
			value1 = l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			value2 = l2.Val
			l2 = l2.Next
		}

		sum = value1 + value2 + carry
		carry = (sum - sum%10) / 10
		lastDigit := sum % 10

		lastNode := &ListNode{Val: lastDigit, Next: nil}

		if dummyHead.Next == nil {
			dummyHead.Next = lastNode
		} else {
			prevlist.Next = lastNode
		}
		prevlist = lastNode

		//takes care of the last carry
		if l1 == nil && l2 == nil && carry != 0 {
			lastNode = &ListNode{Val: carry, Next: nil}
			prevlist.Next = lastNode
		}
	}

	return dummyHead.Next
}

func main() {
	res := addTwoNumbers(
		&ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: &ListNode{}}}},
		&ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4, Next: &ListNode{}}}},
	)

	fmt.Println(res.Val)

}
