


const scriptsInEvents = {

	async Emain_Event16_Act2(runtime, localVars)
	{
		window.parent.squshy.arcade.init();
	},

	async Etitlescreen_Event2_Act1(runtime, localVars)
	{
		(function(){document.querySelector("body").requestFullscreen();})();
	},

	async Etitlescreen_Event23_Act2(runtime, localVars)
	{
		window.parent.squshy.arcade.init();
	},

	async Eenemies_Event72_Act2(runtime, localVars)
	{
		window.parent.squshy.arcade.assignRole({'role': "sbf_kill"});
	},

	async Eenemies_Event108_Act1(runtime, localVars)
	{
		window.parent.squshy.arcade.assignRole({'role': "balloon_kill"});
	},

	async Eenemies_Event243_Act2(runtime, localVars)
	{
		window.parent.squshy.arcade.assignRole({'role': "boss_kill"});
	},

	async Ecredits_Event11_Act2(runtime, localVars)
	{
		window.parent.squshy.arcade.init();
	}

};

self.C3.ScriptsInEvents = scriptsInEvents;

