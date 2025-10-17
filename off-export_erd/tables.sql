create table Product (
    product_id int auto_increment,
    code int not null,
    lc char(2) not null,
    quantity int,
    serving_size int,
    obsolete boolean default 0,
    obsolete_since_date date,
    link varchar(255),
    nova_group decimal(1, 0) not null,
    nova_group_tag varchar(255) not null,
    source_field_publication datetime,
    primary key (product_id)
);

create table Producttranslation (
    product_id int,
    language_code char(2) not null,
    product_translation varchar(255) unique,
    abbreviated_product_translation varchar(255) unique,
    generic_translation varchar(255) unique,
    primary key (product_id, language_code),
    foreign key (product_id) references Product(product_id)
);

create table Producer (
    product_id int,
    producer_product_id int,
    producer_version_id int,
    producer_de varchar(255),
    brand_owner varchar(255),
    primary key (product_id),
    foreign key (product_id) references Product(product_id)
);

create table Brand (
    brand_id int auto_increment,
    brand_name varchar(255) not null unique,
    brand_tag varchar(255) not null unique,
    primary key (brand_id)
);

create table ProductBrand (
    product_id int,
    brand_id int,
    primary key (product_id, brand_id),
    foreign key (product_id) references Product(product_id),
    foreign key (brand_id) references Brand(brand_id)
);

create table Category (
    category_id int auto_increment,
    category_name varchar(255) not null unique,
    category_tag varchar(255) not null unique,
    primary key (category_id)
);

create table ProductCategory (
    product_id int,
    category_id int,
    primary key (product_id, category_id),
    foreign key (product_id) references Product(product_id),
    foreign key (category_id) references Category(category_id)
);

create table Foodgroup (
    food_group_id int auto_increment,
    food_group_name varchar(255) not null unique,
    primary key (food_group_id)
);

create table Foodgrouptag (
    food_group_tag_id int auto_increment,
    food_group_tag_name varchar(255) not null unique,
    primary key (food_group_tag_id)
);

create table FoodgroupFoodgrouptag (
    food_group_id int,
    food_group_tag_id int,
    primary key (food_group_id, food_group_tag_id),
    foreign key (food_group_id) references Foodgroup(food_group_id),
    foreign key (food_group_tag_id) references Foodgrouptag(food_group_tag_id)
);

create table ProductFoodgroup (
    product_id int,
    food_group_id int,
    primary key (product_id, food_group_id),
    foreign key (product_id) references Product(product_id),
    foreign key (food_group_id) references Foodgroup(food_group_id)
);

create table Store (
    store_id int auto_increment,
    store_name varchar(255) not null unique,
    store_tag varchar(255) not null unique,
    primary key (store_id)
);

create table ProductStore (
    product_id int,
    store_id int,
    primary key (product_id, store_id),
    foreign key (product_id) references Product(product_id),
    foreign key (store_id) references Store(store_id)
);

create table Country (
    country_id int auto_increment,
    country_name varchar(255) not null unique,
    country_tag varchar(255) not null unique,
    primary key (country_id)
);

create table ProductCountry (
    product_id int,
    country_id int,
    primary key (product_id, country_id),
    foreign key (product_id) references Product(product_id),
    foreign key (country_id) references Country(country_id)
);




# Column Constraints (not inherited): NOT NULL ↔ DEFAULT NULL/'string'/-x.x +y.y/0,1/date,time,datetime; UNIQUE
# Primary Modifiers: AUTO_INCREMENT (no inheritance necessary) -> automatically increase the value by 1 for each new row. Starting value and increments can be modified
# Referential Actions (Foreign): ON UPDATE / ON DELETE: RESTRICT	-> Prevents deletion/update of parent rows if children exist.
#                                                       SET NULL	-> Sets child column values to NULL if parent is deleted/updated.
#                                                       NO ACTION	-> Similar to RESTRICT (checked at the end of the statement).
#                                                       SET DEFAULT -> Sets child column values to a default value (rarely used in MySQL).