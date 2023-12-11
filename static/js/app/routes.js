let x_routes = {
  "web.login": {x_page:"./static/pages/login.htm?v0.01"},
  "todo.project":{x_page:"./static/pages/todo/project.htm?v0.01",x_code:"/static/pages/todo/project.js"},

  "todo.project_hrdr": {x_api : "/api/project",x_page:"./static/pages/todo/project_hrdr.htm?v0.01",x_code:"/static/pages/todo/project_hrdr.js"},
  "todo.project.edit": {x_api : "/api/project",x_page:"./static/pages/todo/project.htm",x_code:"/static/pages/todo/project.js"},
  "todo.project_list":{x_api: "/api/project",x_page:"./static/pages/todo/project_list.htm?v0.01",x_div:"lstproject_hdr"},

}	

let x_actions = {
  "web.login": {x_act:"post",x_do:"/api/login",x_go:"todo.project_hrdr"},
  "todo.project.save": {x_act:"post",x_do:"/api/project",x_go:"todo.projects"},
  "todo.project.del": {x_act:"del",x_do:"/api/project",x_go:"todo.projects"},
}	
 