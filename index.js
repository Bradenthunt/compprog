function findNeighborhood([x, y], n){
    
    let count = 0
    
    for(let i = 1; i < 15; i++){
        
        for(let j = 1; j < 15; j++){

            let potentialNeighbor = Math.abs(x - i) + Math.abs(y - j)
            
            if (potentialNeighbor <= n){
                count += 1
            }
            
        }
    }
    return count
}

print(findNeighborhood([6,6], 3))