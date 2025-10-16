create table Product (
    product_id int primary key auto_increment,
    code int,
    lc char(2),
    quantity int,
    serving_size int,
    obsolete boolean,
    obsolete_since_date date,
    link varchar(255),
    nova_group decimal(1, 0),
    nova_group_tag varchar(255),
    source_field_publication datetime
);

# NOT NULL; DEFAULT NULL/'string'/?-x+y?; UNIQUE