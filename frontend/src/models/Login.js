import React from 'react';



const LoginForm = ({ isLoginVisible }) => {
    return (
        <section className={`${!isLoginVisible ? "active" : ""} loginShow`} class="vh-100">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                        <div class="card shadow-2-strong" style={{ borderRadius: "1rem" }}>
                            <div class="card-body p-5 text-center">

                                <h3 class="mb-5">Sign in</h3>

                                <div class="form-outline mb-4">
                                    <input type="email" id="typeEmailX-2" class="form-control form-control-lg" />
                                    <label class="form-label" for="typeEmailX-2">Email</label>
                                </div>

                                <div class="form-outline mb-4">
                                    <input type="password" id="typePasswordX-2" class="form-control form-control-lg" />
                                    <label class="form-label" for="typePasswordX-2">Password</label>
                                </div>

                                <div class="form-check d-flex justify-content-start mb-4">
                                    <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
                                    <label class="form-check-label" for="form1Example3"> Remember password </label>
                                </div>

                                <button class="btn btn-primary btn-lg btn-block" type="submit">Login</button>
                                <button class="btn btn-info btn-lg btn-block" type="button" href="#">Register</button>
                                <hr class="my-4"></hr>

                                <button class="btn btn-lg btn-block btn-primary" style={{ backgroundColor: "#dd4b39" }}
                                    type="submit"><i class="fab fa-google me-2"></i> Sign in with google</button>
                                <button class="btn btn-lg btn-block btn-primary mb-2" style={{ backgroundColor: "#3b5998" }}
                                    type="submit"><i class="fab fa-facebook-f me-2"></i>Sign in with facebook</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}


export default LoginForm;