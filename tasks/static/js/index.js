    let dataTable;
    let dataTableUsuarios;
    let dataTableSolicitudes;

    let dataTableIsInitialized = false;
    let dataTableUsuariosIsInitialized = false;
    let dataTableSolicitudesIsInitialized = false;

    const tableBody_requerimientos = document.querySelector("#tableBody_requerimientos");
    const tableBody_usuarios = document.querySelector("#tableBody_usuarios");
    const tableBody_solicitudes = document.querySelector("#tableBody_solicitudes");

const dataTableOptions={
    columnDefs: [
    { className: "centered", targets: [0, 1, 2,] },
    { orderable: false, targets: [1] },
    { searchable: true, targets: [1, 2] }   
    ],
    pageLength: 5,
    destroy: true   
};  

const dataTableUsuariosOptions={
    columnDefs: [
    { className: "centered", targets: [0, 1, 2] },
    { orderable: false, targets: [1] },
    { searchable: true, targets: [1, 2] }
    ],
    pageLength: 5,
    destroy: true
};  

const dataTableSolicitudesOptions={
    columnDefs: [
    { className: "centered", targets: [0, 1] },
    { orderable: false, targets: [1] },
    { searchable: true, targets: [1] }
    ],
    pageLength: 5,
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

const initDateTableUsuarios = async () => {
if(dataTableUsuariosIsInitialized){
    dataTableUsuarios.destroy();
}

await listUsuarios();

dataTableUsuarios=$('#datatable_usuarios').DataTable(dataTableUsuariosOptions);

dataTableUsuariosIsInitialized = true;

};

const initDateTableSolicitudes = async () => {
    if(dataTableSolicitudesIsInitialized){
        dataTableSolicitudes.destroy();
    }
    
    await listSolicitudes();
    
    dataTableSolicitudes=$('#datatable_solicitudes').DataTable(dataTableSolicitudesOptions);
    
    dataTableSolicitudesIsInitialized = true;
    
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
                <td>${task.subcategoria}</td>
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
            </tr>
        `;
        });
        tableBody_usuarios.innerHTML = content;
        console.log(data.users);
    }catch(ex){
        alert(ex);
    }
};

const listSolicitudes = async () =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/list_solicitudes");
        const data = await response.json();

        let content = ``;
        data.solicitudes.forEach((solicitud, index)=>{
        content+=`
            <tr>
                <td>${index + 1}</td>
                <td>${solicitud.comentario}</td>
                <td>${solicitud.user}</td>
                <td>${solicitud.requerimiento}</td>

            </tr>
        `;
        });
        tableBody_solicitudes.innerHTML = content;
        console.log(data.solicitudes);
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

window.addEventListener("load", async () =>{
    await initDateTableSolicitudes();

});