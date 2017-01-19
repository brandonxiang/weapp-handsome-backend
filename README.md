# weapp-handsome-backend
A backend for weapp-handsome

该库为小程序[brandonxiang/weapp-handsome](https://github.com/brandonxiang/weapp-handsome/)的后端部分。

## API

### getValidation

post openid到validation该地址，判断是否存在用户，user代表用户数据，score是投票对应的结果

### getVote

post 投票结果到vote该地址，存新用户openid，更新投票结果

> 该分支采用sqlite，部署到sae的mysql，参考[mysql分支](https://github.com/brandonxiang/weapp-handsome-backend/tree/mysql)
