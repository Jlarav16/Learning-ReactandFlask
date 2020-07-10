import React from 'react';

export const Principal = () => {
    return (
        <div className="">
            <div className='container'>
                <img 
                    className="img-fluid mt-2"
                    src="https://marketingland.com/wp-content/ml-loads/2016/08/grocery-groceries-commerce-online-ss-1920.jpg"
                    alt="J-L products" />
                <hr/>
                <div className="row">
                    <div className="col-md-4 mt-2">
                        <h1>Welcome to Products J&L</h1>
                        <button className="btn btn-primary btn-block">Get started</button>
                    </div>
                    <div className="col-md-8 mt-2 border-left border-primary">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat, voluptas accusamus facere atque, hic tenetur veritatis ullam, consequatur saepe ipsa nobis sequi asperiores fuga libero. Sint, veniam minima modi enim, quisquam placeat delectus ratione debitis tenetur dignissimos impedit libero sunt illum quam, vitae adipisci voluptatum harum rerum ipsa deleniti. Beatae.
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus libero neque, ipsum voluptate natus ea officia praesentium, nam nulla, delectus maiores blanditiis aut iusto. Recusandae.
                        </p>
                    </div>
                </div>
                <hr />
            </div>
        </div>
    );
}