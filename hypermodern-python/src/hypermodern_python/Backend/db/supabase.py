from supabase import Client, create_client


api_url: str = 'https://qpceiciylojzrdtyxcet.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFwY2VpY2l5bG9qenJkdHl4Y2V0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODgxMDQ4MjksImV4cCI6MjAwMzY4MDgyOX0.BqTd4J_WIQ4mXy2lBTz_qx4S_xpyBcIZf6lmcWw-nxM'

def create_supabase_client():
    supabase: Client = create_client(api_url, key)
    return supabase