
document.addEventListener("DOMContentLoaded", function() {
    let dataTable;
    let dataTableUsuarios;
    
    let dataTableIsInitialized = false;
    let dataTableUsuariosIsInitialized = false;
    const tableBody_requerimientos = document.querySelector("#tableBody_requerimientos");
    const tableBody_usuarios = document.querySelector("#tableBody_usuarios"); // Tu código aquí
  });

const dataTableOptions={
    columnDefs: [
    { className: "centered", targets: [0, 1, 2] },
    { orderable: false, targets: [1] },
    { searchable: true, targets: [1, 2] }
    ],
    pageLength: 2,
    destroy: true
};

const dataTableUsuariosOptions={
    columnDefs: [
    { className: "centered", targets: [0, 1, 2] },
    { orderable: false, targets: [1] },
    { searchable: true, targets: [1, 2] }
    ],
    pageLength: 2,
    destroy: true
};  

const initDateTable = async()=>{
if(dataTableIsInitialized){
    dataTable.destroy();
}

await listTasks();

dataTable=$('#datatable_requerimientos').DataTable(dataTableOptions);

dataTableIsInitialized = true;

};

const initDateTableUsuarios = async()=>{
if(dataTableUsuariosIsInitialized){
    dataTableUsuarios.destroy();
}

await listUsuarios();

dataTable=$('#datatable_usuarios').DataTable(dataTableUsuariosOptions);

dataTableUsuariosIsInitialized = true;

};

const listTasks = async () =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/list_tasks");
        const data = await response.json();

        let content = ``;
        data.tasks.forEach((task, index)=>{
        content+=`
            <tr>
                <td>${index + 1}</td>
                <td>${task.nombre}</td>
                <td>${task.categoria}</td>
            </tr>
        `;
        });
        tableBody_requerimientos.innerHTML = content;
        console.log(data.tasks);
    }catch(ex){
        alert(ex);
    }
};

const listUsuarios = async () =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/list_usuarios");
        const data = await response.json();

        let content = ``;
        data.users.forEach((user, index)=>{
        content+=`
            <tr>
                <td>${index + 1}</td>
                <td>${user.first_name}</td>
                <td>${user.last_name}</td>
                <td>${user.email}</td>
                <td>${user.is_admin}</td>
            </tr>
        `;
        });
        tableBody_usuarios.innerHTML = content;
        console.log(data.users);
    }catch(ex){
        alert(ex);
    }
};

window.addEventListener("load", async () =>{
    await initDateTable();

});
window.addEventListener("load", async () =>{
    await initDateTableUsuarios();

});