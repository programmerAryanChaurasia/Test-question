[1:53 pm, 01/08/2024] Aryan Chaurasia: <?php
//array= find 2nd max and 2nd min
//find the duplicate in array

$arr=[1,5,6,8,4,3];

$min1=$arr[0];
$min2=$arr[1];
for($i=0;$i<count($arr);$i++){
    
    if($arr[$i]<$min1){
        $min2=$min1;
        $min1=$arr[$i];
    }
    else if($arr[$i]>$min1){
        if($arr[$i]<$min2){
            $min2=$arr[$i];
        }
    }
}


echo $min2;



?>
[1:54 pm, 01/08/2024] Aryan Chaurasia: <?php
//array= find 2nd max and 2nd min

$arr=[1,5,8,7,6,];

$max1=$arr[0];
$max2=$arr[1];
for($i=0;$i<count($arr);$i++){
    
    
    if($arr[$i]>$max1){
        $max2=$max1;
        $max1=$arr[$i];
    }
    else if($arr[$i]<$max1){
        if($arr[$i]>$max2){
            $max2=$arr[$i];
        }
    }
}

// echo $max1." ";
echo $max2;



?>
[1:54 pm, 01/08/2024] Aryan Chaurasia: '''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


# arr=[1,2,2,2,4,5,9,9];

# length=len(arr)
# # print(length)

# d={}


# while(length!=0):
#     if arr[length] in d:
#         d[arr[length]]=d[arr[length]]+1
#         pass
#     else:
#         d[length]=1
#     length-=1
arr = [1, 2, 2, 2, 4, 5, 9, 9,1,1,1,1,1,1,7,1,1,7,7,7]

length = len(arr) - 1
d = {}

while length >= 0:
    if arr[length] in d:
        d[arr[length]] += 1
    else:
        d[arr[length]] = 1
    length -= 1

print(d)

# print(d)