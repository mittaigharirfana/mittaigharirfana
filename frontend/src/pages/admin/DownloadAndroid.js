import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Download, ArrowLeft, Smartphone } from 'lucide-react';
import { Button } from '../../components/ui/button';

const DownloadAndroid = () => {
  const navigate = useNavigate();

  const handleDownload = () => {
    // Create a download link
    const link = document.createElement('a');
    link.href = `${process.env.REACT_APP_BACKEND_URL}/api/download-android`;
    link.download = 'freshwala-android.tar.gz';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex items-center space-x-4 mb-8">
          <Button
            onClick={() => navigate('/admin/dashboard')}
            variant="outline"
            size="sm"
          >
            <ArrowLeft size={16} className="mr-2" />
            Back to Dashboard
          </Button>
          <h1 className="text-3xl font-bold text-gray-900">Download Android Project</h1>
        </div>

        <div className="bg-white rounded-lg shadow-md p-8">
          <div className="text-center space-y-6">
            <div className="w-24 h-24 bg-green-100 rounded-full flex items-center justify-center mx-auto">
              <Smartphone className="text-green-600" size={48} />
            </div>

            <h2 className="text-2xl font-bold text-gray-900">
              Your Android App is Ready!
            </h2>

            <p className="text-gray-600">
              Download the Android project files to publish on Google Play Store
            </p>

            <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 text-left">
              <h3 className="font-semibold text-gray-900 mb-3">What's included:</h3>
              <ul className="space-y-2 text-sm text-gray-700">
                <li>✅ Complete Android project configured with Capacitor</li>
                <li>✅ Package name: com.freshwala.app</li>
                <li>✅ Ready to open in Android Studio</li>
                <li>✅ All web features converted to Android app</li>
              </ul>
            </div>

            <Button
              onClick={handleDownload}
              className="bg-green-600 hover:bg-green-700 text-white px-8 py-6 text-lg font-semibold"
            >
              <Download size={24} className="mr-3" />
              Download Android Project (992 KB)
            </Button>

            <div className="border-t pt-6 mt-6">
              <h3 className="font-semibold text-gray-900 mb-3">Next Steps:</h3>
              <ol className="text-left space-y-3 text-sm text-gray-700">
                <li>1. Download and extract the project files</li>
                <li>2. Open Android Studio</li>
                <li>3. Click "Open an Existing Project"</li>
                <li>4. Navigate to the extracted "android" folder</li>
                <li>5. Follow the Play Store deployment guide</li>
              </ol>
            </div>

            <div className="bg-orange-50 border border-orange-200 rounded-lg p-4 text-sm text-gray-700">
              📚 <strong>Need help?</strong> Check the complete guide at:
              <code className="ml-2 bg-white px-2 py-1 rounded">/app/PLAYSTORE_DEPLOYMENT_GUIDE.md</code>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DownloadAndroid;
