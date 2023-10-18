/** @odoo-module **/

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart } = owl;
import { useService } from "@web/core/utils/hooks";

export class TodoTask extends Component {
    setup() {
        this.state = useState({
            taskList: [],
        });
        this.orm = useService("orm")
        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead('todo.task', [], ["name", "color", "is_done", "description"])
    }

}

TodoTask.template = 'module_owl.TodoTask';
registry.category('actions').add('module_owl.action_todo_task_js', TodoTask);