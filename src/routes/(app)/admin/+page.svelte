<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	onMount(() => {
		// redirect only when user is exactly on /admin
		if ($page.url.pathname === '/admin') {
			goto('/admin/users');
		}
	});
</script>