/** @odoo-module **/

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

export class TodoTask extends Component {
    setup() {
        this.state = useState({
            task:{name:"", color:"#000000", description:"", is_done:false},
            taskList:[],
            isEdit: false,
            activeId: false,
        });
        this.orm = useService("orm")
        this.model = "todo.task"
        this.searchInput = useRef("search-input")
        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "color", "is_done", "description"])
    }

    addTask(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }
    
    editTask(task){
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = {...task}
    }

    resetForm(){
        this.state.task = {name:"", color:"#000000", description:"", is_done:false}
    }

    async saveTask(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }

        await this.getAllTasks()
    }

    async deleteTask(task){
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()
    }

    async searchTasks(){
        const text = this.searchInput.el.value
        this.state.taskList = await this.orm.searchRead(this.model, [['name','ilike',text]], ["name", "color", "is_done", "description"])
    }

    async updateColor(e, task){
        await this.orm.write(this.model, [task.id], {color: e.target.value})
        await this.getAllTasks()
    }

}

TodoTask.template = 'module_owl.TodoTask';
registry.category('actions').add('module_owl.action_todo_task_js', TodoTask);