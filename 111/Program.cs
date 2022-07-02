namespace problem111 {
    class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    class MainClass {         
        static int answer = Int32.MaxValue;

        static void MinDepth(TreeNode root, int depth = 0) {
            if (root is not null) {
                if (depth > answer) {
                    return;
                }
                if (root.right is null && root.left is null) {
                    answer = depth;
                } else {
                    if (root.right is not null) {
                        MinDepth(root.right, ++depth);
                    }
                    if (root.left is not null) {
                        MinDepth(root.left, ++depth);
                    }
                }
            }
            return; 
        }

        static int solution(TreeNode root) {
            MinDepth(root);
            int tempAnswer = answer;
            answer = Int32.MaxValue;
            return tempAnswer;
        }

        static void Main(string[] args) {
            TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
            Console.WriteLine(solution(root));

            TreeNode root2 = new TreeNode(2, null, new TreeNode(3, null, new TreeNode(4, null, new TreeNode(5, null, new TreeNode(6)))));
            Console.WriteLine(solution(root2));
        }
    }
}