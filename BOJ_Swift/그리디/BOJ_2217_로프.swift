import Foundation

func getMaxLopeProduct() -> Int {
    let n = Int(readLine()!)!
    var lope = [Int]()
    var res = [Int]()
    
    for _ in 0..<n {
        lope.append(Int(readLine()!)!)
    }
    
    lope.sort()
    
    for i in 0..<n {
        res.append(lope[i] * (n - i))
    }
    
    return res.max() ?? 0
}

print(getMaxLopeProduct())
