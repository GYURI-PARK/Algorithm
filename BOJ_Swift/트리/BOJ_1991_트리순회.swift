class Graph<T: Hashable> {
    var nodes = [T: Node]()
    
    class Node {
        var value: T
        var leftNode: Node?
        var rightNode: Node?
        
        init(_ value: T) {
            self.value = value
        }
    }
    
    func addChild(node: T, left: T?, right: T?) {
        if nodes[node] == nil {
            nodes[node] = Node(node)
        }
        if let left = left {
            nodes[node]?.leftNode = nodes[left, default: Node(left)]
        }
        if let right = right {
            nodes[node]?.rightNode = nodes[right, default: Node(right)]
        }
    }
    
    func preorder(at node: T, history: inout [T]) {
        history.append(node)
        if let left = nodes[node]?.leftNode {
            preorder(at: left.value, history: &history)

        }
        
        if let right = nodes[node]?.rightNode {
            preorder(at: right.value, history: &history)
        }
    }
    
    func inorder(at node: T, history: inout [T]) {
        if let left = nodes[node]?.leftNode {
            inorder(at: left.value, history: &history)
        }
        history.append(node)
        if let right = nodes[node]?.rightNode {
            inorder(at: right.value, history: &history)
        }
    }
    
    func postorder(at node: T, history: inout [T]) {
        if let left = nodes[node]?.leftNode {
            postorder(at: left.value, history: &history)
        }
        if let right = nodes[node]?.rightNode {
            postorder(at: right.value, history: &history)
        }
        history.append(node)
    }
}

var graph = Graph<Character>()
let n = Int(readLine()!)!
for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { $0 == "." ? nil : Character(String($0)) }
    graph.addChild(node: input[0]!, left: input[1], right: input[2])
}

var travel = [Character]()
graph.preorder(at: graph.nodes["A"]!.value, history: &travel)
print(String(travel))
travel.removeAll()
graph.inorder(at: graph.nodes["A"]!.value, history: &travel)
print(String(travel))
travel.removeAll()
graph.postorder(at: graph.nodes["A"]!.value, history: &travel)
print(String(travel))