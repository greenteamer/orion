// Input (JSX):
define(['react', 'Auth', 'Registration', 'AppActions'], function (React, Auth, Registration, AppActions) {

    var Navigation = React.createClass({
        displayName: 'Navigation',
        logoutUserButtonClick: function () {
            AppActions.logout();
        },
        render: function () {
            if (this.props.user.username !== 'Незарегистрированный') {
                return (
                    React.createElement("nav", {id: "top-menu", className: "navbar navbar-default", role: "navigation"}, 
    				  	React.createElement("div", {className: "container-fluid"}, 
    					   	React.createElement("div", {className: "navbar-header"}, 
    					      	React.createElement("button", {type: "button", className: "navbar-toggle collapsed", "data-toggle": "collapse", "data-target": "#not-google-plus-nav"}, 
    						        React.createElement("span", {className: "sr-only"}, "Toggle Navigation"), 
    						        React.createElement("span", {className: "icon-bar"}), 
    						        React.createElement("span", {className: "icon-bar"}), 
    						        React.createElement("span", {className: "icon-bar"})
    					      	), 
    					      	React.createElement("a", {className: "navbar-brand", href: "/"}, "Репетитор")
    					    ), 

    					    React.createElement("div", {className: "collapse navbar-collapse", id: "not-google-plus-nav"}, 
    					      	React.createElement("ul", {className: "nav navbar-nav pull-right"}, 
    					          	React.createElement("li", null, React.createElement("a", {href: "/+current_user"}, this.props.user.username)), 
    					          	React.createElement("li", null, React.createElement("a", {href: "/+current_user/settings"}, "Настройки")), 
                                    React.createElement("li", null, React.createElement("a", {href: "javascript:void(0)", onClick: this.logoutUserButtonClick}, "Выйти"))
    					      	)
    					    )
    			 		)
    				)
                )
            } else {
                return (
                    React.createElement("nav", {id: "top-menu", className: "navbar navbar-default", role: "navigation"}, 
                        React.createElement("div", {className: "container-fluid"}, 
                            React.createElement("div", {className: "navbar-header"}, 
                                React.createElement("button", {type: "button", className: "navbar-toggle collapsed", "data-toggle": "collapse", "data-target": "#not-google-plus-nav"}, 
                                    React.createElement("span", {className: "sr-only"}, "Toggle Navigation"), 
                                    React.createElement("span", {className: "icon-bar"}), 
                                    React.createElement("span", {className: "icon-bar"}), 
                                    React.createElement("span", {className: "icon-bar"})
                                ), 
                                React.createElement("a", {className: "navbar-brand", href: "/"}, "Репетитор")
                            ), 

                            React.createElement("div", {className: "collapse navbar-collapse", id: "not-google-plus-nav"}, 
                                React.createElement("ul", {className: "nav navbar-nav pull-right"}, 
                                    React.createElement("li", null, React.createElement("a", {href: "#"}, this.props.user.username)), 
                                    React.createElement("li", null, React.createElement("a", {href: "javascript:void(0)"}, "Зарегистрироваться")), 
                                    React.createElement("li", null, 
                                        React.createElement("a", {id: "login_button", className: "", href: "", "data-toggle": "modal", "data-target": "#login-dialog"}, "Войти")
                                    ), 
                                    React.createElement("li", null, React.createElement(Auth, null)), 
                                    React.createElement("li", null, React.createElement(Registration, null))
                                )
                            )
                        )
    				)
                )
            }
        }
    });

    return Navigation;
});
