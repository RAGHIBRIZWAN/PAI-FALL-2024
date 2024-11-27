income <- 100000

if(income < 30000){
    print(paste("Final income: ",income))
}else if(income >= 30000 && income < 70000){
    final <- income + income*0.1
    print(paste("Final income: ",final))
}else if(income >= 70000 && income < 100000){
    final <- income + income*0.15
    print(paste("Final income: ",final))
}else if(income >= 100000){
    final <- income + income*0.2
    print(paste("Final income: ",final))
}
