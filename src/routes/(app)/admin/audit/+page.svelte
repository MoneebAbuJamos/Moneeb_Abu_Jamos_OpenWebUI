<script lang="ts">
	import { onMount } from "svelte";

	let logs = [];
	let loading = true;

	async function loadLogs() {
		try {
			const res = await fetch("/api/v1/audit/logs");
			logs = await res.json();
		} catch (err) {
			console.error("Failed to load audit logs", err);
		} finally {
			loading = false;
		}
	}

	onMount(loadLogs);
</script>

<div class="p-6">

	<h1 class="text-xl font-semibold mb-4">Audit Logs</h1>

	{#if loading}
		<p>Loading logs...</p>

	{:else if logs.length === 0}
		<p>No audit logs found.</p>

	{:else}

	<table class="w-full text-sm border border-gray-700">
		<thead class="bg-gray-800">
			<tr>
				<th class="p-2 text-left">Event</th>
				<th class="p-2 text-left">User</th>
				<th class="p-2 text-left">Message</th>
				<th class="p-2 text-left">Time</th>
			</tr>
		</thead>

		<tbody>
			{#each logs as log}
			<tr class="border-t border-gray-700">
				<td class="p-2">{log.event_type}</td>
				<td class="p-2">{log.actor_email}</td>
				<td class="p-2">{log.message}</td>
				<td class="p-2">{log.created_at}</td>
			</tr>
			{/each}
		</tbody>
	</table>

	{/if}

</div>