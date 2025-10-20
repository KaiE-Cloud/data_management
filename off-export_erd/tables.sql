



# Core Product & Identification

create table Product (
    product_id int auto_increment,
    code int not null,
    lc char(2) not null,
    quantity int,
    serving_size int,
    obsolete boolean default 0,
    obsolete_since_date date,
    link varchar(255),
    nova_group decimal(1, 0) not null default 4,
    nova_group_tag varchar(255) not null default 'en:4-ultra-processed-food-and-drink-products',
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
    foreign key (product_id) references Product(product_id) on delete cascade
);

create table Producer (
    product_id int,
    producer_product_id int,
    producer_version_id int,
    producer_de varchar(255),
    brand_owner varchar(255),
    primary key (product_id),
    foreign key (product_id) references Product(product_id) on delete cascade
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
    foreign key (product_id) references Product(product_id) on delete cascade,
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
    foreign key (product_id) references Product(product_id) on delete cascade,
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
    foreign key (food_group_id) references Foodgroup(food_group_id) on delete cascade,
    foreign key (food_group_tag_id) references Foodgrouptag(food_group_tag_id)
);

create table ProductFoodgroup (
    product_id int,
    food_group_id int,
    primary key (product_id, food_group_id),
    foreign key (product_id) references Product(product_id) on delete cascade,
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
    foreign key (product_id) references Product(product_id) on delete cascade,
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
    foreign key (product_id) references Product(product_id) on delete cascade,
    foreign key (country_id) references Country(country_id)
);




# Composition & Ingredients

create table Ingredient (
    ingredient_id int auto_increment,
    ingredient_name varchar(255) not null unique,
    primary key (ingredient_id)
);

create table ProductIngredient (
    product_id int,
    ingredient_id int,
    primary key (product_id, ingredient_id),
    foreign key (product_id) references Product(product_id) on delete cascade,
    foreign key (ingredient_id) references Ingredient(ingredient_id)
);

create table Ingredienttranslation (
    ingredient_id int,
    language_code char(2),
    ingredient_translation varchar(255) not null unique,
    primary key (ingredient_id, language_code),
    foreign key (ingredient_id) references Ingredient(ingredient_id) on delete cascade
);

create table Allergen (
    allergen_id int auto_increment,
    allergen_name varchar(255) not null unique,
    allergen_tag varchar(255) not null unique,
    primary key (allergen_id)
);

create table Trace (
    trace_id int auto_increment,
    trace_name varchar(255) not null unique,
    trace_tag varchar(255) not null unique,
    primary key (trace_id)
);

create table ProductAllergen (
    product_id int,
    allergen_id int,
    primary key (product_id, allergen_id),
    foreign key (product_id) references Product(product_id) on delete cascade,
    foreign key (allergen_id) references Allergen(allergen_id)
);

create table ProductTrace (
    product_id int,
    trace_id int,
    primary key (product_id, trace_id),
    foreign key (product_id) references Product(product_id) on delete cascade,
    foreign key (trace_id) references Trace(trace_id)
);

create table Origin (
    product_id int,
    origin_name varchar(255),
    origin_tag varchar(255),
    manufacturing_place varchar(255),
    manufacturing_place_tag varchar(255),
    emb_code varchar(255),
    emb_code_tag varchar(255),
    primary key (product_id),
    foreign key (product_id) references Product(product_id) on delete cascade
);

create table Origintranslation (
    product_id int,
    language_code char(2),
    origin_translation varchar(255) not null unique,
    primary key (product_id, language_code),
    foreign key (product_id) references Product(product_id) on delete cascade
);

create table Packaging (
    product_id int,
    packaging_level decimal(1, 0),
    packaging_number_of_units int,
    packaging_shape varchar(255),
    packaging_material varchar(255),
    packaging_recycling varchar(255),
    packaging_weight_measured int,
    primary key (product_id, packaging_level),
    foreign key (product_id) references Product(product_id) on delete cascade
);

create table Packagingtype (
    packaging_type_id int auto_increment,
    packaging_type_name varchar(255) not null unique,
    packaging_type_tag varchar(255) not null unique,
    primary key (packaging_type_id)
);

create table ProductPackagingtype (
    product_id int,
    packaging_type_id int,
    primary key (product_id, packaging_type_id),
    foreign key (product_id) references Product(product_id) on delete cascade,
    foreign key (packaging_type_id) references Packagingtype(packaging_type_id)
);




# Nutrition

create table Nutrientfact (
    product_id int,
    nutrient_name varchar(255),
    nutrient_value double not null,
    nutrient_prepared_value double not null,
    unit_id int not null,
    primary key (product_id, nutrient_name),
    foreign key (product_id) references Product(product_id) on delete cascade,
    foreign key (nutrient_name) references Nutrient(nutrient_name),
    foreign key (unit_id) references Unit(unit_id)
);

create table Nutrient (
    nutrient_name varchar(255),
    nutrient_group varchar(255) not null,
    unit_id int not null,
    primary key (nutrient_name),
    foreign key (unit_id) references Unit(unit_id)
);

create table Unit (
    unit_id int auto_increment,
    unit_name varchar(255) not null unique,
    unit_symbol varchar(255) not null unique,
    conversion_factor_to_base double not null,
    primary key (unit_id)
);

create table Nutritionfact (
    product_id int,
    nutrition_data_per varchar(255) not null default '100g',
    nutrition_data_prepared_per varchar(255) not null default '100g',
    primary key (product_id),
    foreign key (product_id) references Product(product_id) on delete cascade
);




# Classification & Scoring




# Column Constraints (not inherited): NOT NULL ↔ DEFAULT NULL/'string'/-x.x +y.y/0,1/date,time,datetime; UNIQUE
# Primary Modifier: AUTO_INCREMENT (no inheritance necessary) -> automatically increase the value by 1 for each new row. Starting value and increments can be modified
# Referential Actions (Foreign): ON UPDATE / ON DELETE -> CASCADE	  -> Updates/deletes child rows when parent is updated/deleted
#                                                         SET NULL	  -> Sets child column values to NULL if parent is updated/deleted
#                                                         SET DEFAULT -> Sets child column values to a default value (rarely used in MySQL)
#                                                         RESTRICT	  -> Prevents deletion/update of parent row if child rows exist (checked immediately)
#                                                         NO ACTION	  -> Similar to RESTRICT, but checked at the end of the statement