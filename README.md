# weapp-handsome-backend
A backend for weapp-handsome


## API

### getValidation

post openid到validation该地址，判断是否存在用户，user代表用户数据，score是投票对应的结果

### getVote

post 投票结果到vote该地址，存新用户openid，更新投票结果


## mysql branch

mysql分支是针对sae部署，表结构保持一致，[sql语句](app_brandonhandsome.sql)


### validation表的字段

- id int(11)
- openid text

### vote表的字段

- name text
- score int