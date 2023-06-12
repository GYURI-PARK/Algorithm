let n = Int(readLine()!)!

for _ in 0..<n {
    var stack = []
    let s = readLine()!
    for a in s {
        if a == "(" {
            stack.append(a)
        } 
        else if String(a) == ")" {
            if len(stack) == 0 {
                print("NO")
                break
            } else {
                stack.pop()
            }
        }
    }
    if len(stack) == 0 {
        print("YES")
    } else {
        print("NO")
    }
}
